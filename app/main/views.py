from flask import Flask, render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
 
app = Flask(__name__)
from app import app
 
app.config['SECRET_KEY'] = 'd7b1a25b72b817d78afffe763942756b42b01564'
 
 
 
 
posts = [
   {
       'author': 'David',
       'name': 'human'
   },
   {
       'author': 'Agg',
       'name': 'human2'
   }
]
 
 
 
# Views
@app.route('/')
@app.route('/home')
def index():
   '''
   View root page function that returns the index page and its data
   ''' 
   return render_template('home.html',posts = posts)
 
@app.route('/about')
def about():
 
   '''
   View root page function that returns the index page and its data
   '''
 
   about_page= 'Into the'
   return render_template('about.html',title = 'About')
 
 
@app.route("/register", methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       flash(f'Account created for {form.username.data}!', 'success')
       return redirect(url_for('home'))
   return render_template('register.html', title='Register', form=form)
 
 
@app.route("/login", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
       if form.email.data == 'admin@blog.com' and form.password.data == 'password':
           flash('You have been logged in!', 'success')
           return redirect(url_for('home'))
       else:
           flash('Login Unsuccessful. Please check username and password', 'danger')
   return render_template('login.html', title='Login', form=form)