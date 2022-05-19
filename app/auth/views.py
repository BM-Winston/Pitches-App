from flask import render_template, url_for, flash, redirect, request
from . import auth
from ..email import mail_message
from .forms import SignInForm, SignUpForm
from ..models import User
from ..import db
from flask_login import login_user, login_required,  logout_user



@auth.route('/signup', methods = ["GET","POST"])
def signup():
  form = SignUpForm()
  if form.validate_on_submit():
    user = User(email = form.email.data, username = form.username.data, password = form.password.data)
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))
  return render_template('auth/signup.html', signup_form = form)


@auth.route('/login', methods = ['GET','POST'])
def login():
  signin_form = SignInForm()
  if signin_form.validate_on_submit():
    user = User.query.filter_by(email = signin_form.email.data).first()
    if user is not None and user.verify_password(signin_form.password.data):
      login_user(user,signin_form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid Username or Password')
  title = "Pitches"
  return render_template('auth/signin.html', signin_form=signin_form,title=title)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))