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
