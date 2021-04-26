from flask import Flask, render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User , Post
from . import Auth , auth

#Havent installed the import db
#Sent email to retriev the information
#db.create_all
# site.db file not created
# from views import User, Post
# user_1 = user(username='Alex', email='x.com', password =''password) 
#db.session.add(user_1)
#user_2 = user(username='Alex1', email='x1.com', password =''1password) 
#db.session.add(user_2)
#db.session.commit()
#User.query.all() ---> All users
#User.query.first() 
#User.query.filter_by(username=''Alex).all() ---All username with the name Alex
#user = User.query.filter_by(username=''Alex).first()
#user = User.query.get(1) -->User I
#user.posts --> To kno the posts gotten
#post_1 = Post(title = 'Blog', content = 'First POst Content!' , user_id= user.id)
#post_2 = Post(title = 'Blog1', content = 'First POst Content2!' , user_id= user.id)
#db.session.add(post_1)
#db.session.add(user_2)
#db.session.commit()
#user.posts
# post = Post.query.first() ---> #>post
#post.user_id
# post.author --->get all the user information






 
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
@apply().route('/')
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

#@auth.route('/login')
#def login():
 #   return render_template('auth/login.html')