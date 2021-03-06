import os
from .forms import RegistrationForm,LoginForm
from . import auth
from flask import render_template,redirect,url_for,flash,request
from .. import db,mail
from .. models import User
from ..send_mail import mail_message
from flask_login import login_user,logout_user,login_required

# @main.route('/')
# def index():
#     return render_template ('index.html')

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Your account has been succesfully Created. Proceed to login","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    return render_template ('register.html')

@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitches login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
