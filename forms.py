from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
# from app import Users


class UpdateAccountForm(FlaskForm):
    first_name = StringField(
        'First name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    last_name = StringField(
        'Last name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField(
        'Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField('Update')

    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         user = Users.query, filter_by(email=email.data).first()
    #         if user:
    #             raise ValidationError('Email already in use.')


class PlantsForm(FlaskForm):
    plant_name = StringField(
        'Plant Name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    plant_nick = StringField(
        'Plant Nickname',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    plant_desc = StringField(
        'Plant Description',
        validators=[
            DataRequired(),
            Length(min=2, max=200)
        ]
    )

    plant_notes = StringField(
        'Additional Notes',
        validators=[
            DataRequired(),
            Length(min=2, max=300)
        ]
    )

    submit = SubmitField('Make a post.')


class SignInForm(FlaskForm):

    email = StringField(
        'Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password: ',
        validators=[
            DataRequired(),
            Length(min=1, max=64)
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In.')


class SignUpForm(FlaskForm):

    first_name = StringField(
        'First name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    last_name = StringField(
        'Last name: ',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    email = StringField(
        'Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = StringField(
        'Password: ',
        validators=[
            DataRequired(),
        ]
    )

    confpassword = StringField(
        'Confirm Password: ',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Sign Up.')

