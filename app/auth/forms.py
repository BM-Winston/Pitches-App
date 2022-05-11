from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Email,EqualTo
from ..models import User


class SignUpForm(FlaskForm):
    email = StringField('Your Email Address',validators = [Email()])
    username = StringField('Enter Your Username')
    password = PasswordField('Password',validators = [EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords')
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Email()])
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')