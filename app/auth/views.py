from flask import render_template,request,redirect, url_for, flash
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
        
    title = "Login"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.form
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        confirm_password = form.get("confirm_password")
        if username is None or password is None or email is None or confirm_password is None:
            error = 'username, email, password are required'
            return render_template('signup.html', error=error)
        if ' ' in username:
            error = 'Username should not contain spaces'
            return render_template('signup.html', error=error)
        if password != confirm_password:
            error = "Passwords do not match"
            return render_template('signup.html', error=error)
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                error = 'A user with that name already exists'
                return render_template('signup.html', error=error)
            user = User.query.filter_by(email=email).first()
            if user is not None:
                error = 'A user with that email already exists'
                return render_template('signup.html', error=error)
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect(url_for('auth.login'))

    return render_template('register.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))