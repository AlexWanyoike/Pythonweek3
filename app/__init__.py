from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
from app import app , db , create_app
from app.models import User
app.config['SECRET_KEY'] = 'd7b1a25b72b817d78afffe763942756b42b01564'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# Initializing application


app = Flask(__name__)


from app.main import views