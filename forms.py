from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


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
    username = StringField(
        'Desired Username: ',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    email = StringField(
        'Email: ',
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

    confpassword = StringField(
        'Confirm Password: ',
        validators=[
            DataRequired(),
            Length(min=1, max=64)
        ]
    )

    submit = SubmitField('Sign Up.')