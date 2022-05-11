from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms import validators 
from wtforms.fields.choices import SelectField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = StringField('Pitch Category',choices = [('Pick-up Lines','Pick-up Lines'),('Interview','Interview'),('Product','Product'),('Promotion','Promotion'),('Music','Music'),('Sports','Sports')]) 
    context = TextAreaField('Pitch it')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Comment title')
    comment = TextAreaField('Pitch comment')
    submit = SubmitField('Submit')

