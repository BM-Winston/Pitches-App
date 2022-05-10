from flask_wtf import Flaskform
from wtform import TextAreaField, StringField, SubmitField
from wtforms import validators


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.')
    submit = SubmitField('Submit')

