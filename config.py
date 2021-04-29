
import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/pitches'
    

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://gkfqbhhevqcfnd:db4d3d926414b13d841f3e32931ae4bb9407aa333479a410534e283097f97e52@ec2-34-200-94-86.compute-1.amazonaws.com:5432/d9tuj4uncf9us6?sslmode=require'
  


class DevConfig(Config):
    
    DEBUG = True
    

class TestConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig

}