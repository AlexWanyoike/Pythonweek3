from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask import Blueprint
#from .auth import auth as auth_blueprint

#app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)

    
    
    return app

auth = Blueprint('auth',__name__)

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