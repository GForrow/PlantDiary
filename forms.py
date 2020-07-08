from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from app import Users


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

    username = StringField(
        'Username: ',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    password = StringField(
        'Password: ',
        validators=[
            DataRequired(),
            Length(min=1, max=64)
        ]
    )

    submit = SubmitField('Sign In.')


class SignUpForm(FlaskForm):

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

