import os
from flask_mail import Mail

class Config:
    SECRET_KEY='Sqp1aHMA1U'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andy:Access@localhost/school'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST ="app/static/photos"
    MAIL_SERVER = 'smtp.googlemail.com' 
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andy:Access@localhost/school'

    

class ProdConfig(Config):
    '''
    Production  configuration child class
    
    '''
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andy:Access@localhost/school'
    





class DevConfig(Config):
  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andy:Access@localhost/school'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}