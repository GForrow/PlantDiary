from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import PlantsForm, SignInForm, SignUpForm, UpdateAccountForm
from flask_bcrypt import Bcrypt
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from datetime import datetime


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'


app.config['SECRET_KEY'] = environ.get('PLANTAPP_SECRETKEY')
app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASS') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_plantdb')

db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(30), nullable=False)
    plant_nick = db.Column(db.String(30), nullable=True)
    plant_desc = db.Column(db.String(100), nullable=False)
    plant_notes = db.Column(db.String(300), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'User ID: ', self.user_id, '\r\n',
                'Title: ', self.plant_name, '\r\n', self.plant_desc
            ]
        )


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n',
                        'Email: ', self.email, '\r\n',
                       'Name: ', self.first_name, ' ', self.last_name])


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage')


@app.route('/updateaccount', methods=['GET','POST'])
@login_required
def updateaccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('updateaccount'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('updateaccount.html', title='Update Account', form=form)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = SignInForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('account'))
    return render_template('signin.html', title='Sign In', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    post = current_user.id
    #post_data = Posts.query.all()
    post_data = Posts.query.filter_by(user_id=post)
    return render_template('account.html', title='My Account', plants=post_data)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )
        print(user)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('account'))
    else:
        print("not working")
        return render_template('signup.html', title='Sign Up', form=form)


@app.route('/newplant', methods=['GET', 'POST'])
def newentry():
    form = PlantsForm()
    if form.validate_on_submit():
        post_data = Posts(
            plant_name=form.plant_name.data,
            plant_nick=form.plant_nick.data,
            plant_desc=form.plant_desc.data,
            plant_notes=form.plant_notes.data,
            user_id=Users.get_id(current_user)
        )
        db.session.add(post_data)
        db.session.commit()

        return redirect(url_for('account'))
    else:
        return render_template('newentry.html', title='New Plant', form=form)


@app.route('/create')
def create():
    db.create_all()
    return "Added table and populated with dummy records"


@app.route('/delete')
def delete():
    db.session.query(Posts).delete()
    db.session.commit()
    db.drop_all()
    return "It's all gone."


@app.route("/updateaccount/delete", methods=['GET', 'POST'])
@login_required
def account_delete():
    user = current_user.id
    post = current_user.id
    accounttodelete = Users.query.filter_by(id=user).first()
    poststodelete = Posts.query.filter_by(user_id=post).all()
    logout_user()
    db.session.delete(accounttodelete)
    db.session.delete(poststodelete)
    print("delete account")
    db.session.commit()
    return redirect(url_for('signup'))


def validate_email(self, email):
    user = Users.query.filter_by(email=email.data).first()

    if user:
        raise ValidationError('Email already in use.')


if __name__ == '__main__':
    app.run()
