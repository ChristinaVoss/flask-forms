from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class ClubForm(FlaskForm):
    name = StringField('Club name', validators=[InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Club Description', validators=[InputRequired(), Length(max=200)])
    spaces_available = IntegerField('Spaces available', validators=[InputRequired()])
    time_of_day = RadioField('When will the club be running?', choices=['Morning', 'Lunch time', 'After school'], validators=[InputRequired()])
    is_free = BooleanField('Free club', default='checked')
    submit = SubmitField("Create club")
