from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import PlantsForm, SignInForm, SignUpForm
from flask_bcrypt import Bcrypt
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


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

    def __repr__(self):
        return ''.join(
            [
                'Plant: ' + self.plant_name + ' Nickname: ' + self.plant_nick + '\n'
                                              'Description: ' + self.plant_desc + '\n'
                                                                                  'Notes: ' + self.plant_notes
            ]
        )


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage')


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

    # form = SignInForm()
    # if form.validate_on_submit():
    #     post_data = Posts(
    #         username=form.username.data,
    #         password=form.password.data,
    #     )
    #     db.session.add(post_data)
    #     db.session.commit()
    #
    #     return redirect(url_for('account'))
    # else:
    #     return render_template('signin.html', title='Sign In', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    post_data = Posts.query.all()
    return render_template('account.html', title='My Account', plants=post_data)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(email=form.email.data, password=hash_pw)
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
            plant_notes=form.plant_notes.data
        )
        db.session.add(post_data)
        db.session.commit()

        return redirect(url_for('account'))
    else:
        return render_template('newentry.html', title='New Plant', form=form)


@app.route('/create')
def create():
    db.create_all()
    # plant1 = Posts(plant_name="", plant_desc="", plant_nick="", plant_notes="")
    # plant2 = Posts(plant_name="", plant_desc="", plant_nick="", plant_notes="")
    # db.session.add(plant1)
    # db.session.add(plant2)
    # db.session.commit()
    return "Added table and populated with dummy records"


@app.route('/delete')
def delete():
    db.session.query(Posts).delete()
    db.session.commit()
    return "It's all gone."


def validate_email(self, email):
    user = Users.query.filter_by(email=email.data).first()

    if user:
        raise ValidationError('Email already in use.')


if __name__ == '__main__':
    app.run()
