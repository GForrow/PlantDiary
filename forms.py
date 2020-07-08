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

    l_name = StringField(
        'Plant Nickname',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    title = StringField(
        'Plant Description',
        validators=[
            DataRequired(),
            Length(min=2, max=200)
        ]
    )

    content = StringField(
        'Additional Notes',
        validators=[
            DataRequired(),
            Length(min=2, max=300)
        ]
    )

    submit = SubmitField('Make a post.')