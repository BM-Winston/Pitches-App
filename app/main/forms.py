from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField
from wtforms.validators import  InputRequired

# from wtforms.fields.choices import 



class PitchForm(FlaskForm):
    category = SelectField('Pitch Category',choices=[('Pick-up Lines','Pick-up Lines'),('Interview','Interview'),('Product','Product'),('Promotion','Promotion'),('Music','Music'),('Sports','Sports')]) 
    context = TextAreaField('Pitch it',validators = [InputRequired()])
    submit = SubmitField('Submit')

    # 


class CommentForm(FlaskForm):
    title = StringField('Comment title')
    comment = TextAreaField('Pitch comment')
    submit = SubmitField('Submit')



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.')
    submit = SubmitField('Submit')



