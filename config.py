
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='d7b1a25b72b817d78afffe763942756b42b01564'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:12345@localhost/pitch'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alex:1234@localhost/pitch'

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig

}