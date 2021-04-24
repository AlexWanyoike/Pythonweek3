from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)

#app.config['SECRET_KEY'] = 'd7b1a25b72b817d78afffe763942756b42b01564'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db.init_app(app)

#
#from config import Config
#from flask_migrate import Migrate


#app = Flask(__name__)
#db.init_app(app)
#migrate = Migrate(app, db)

#from app.models import User

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initializing application

#from app import views 