import os
from flask_mail import Mail

class Config:
    SECRET_KEY='Sqp1aHMA1U'
    UPLOADED_PHOTOS_DEST =
    MAIL_SERVER = 
    MAIL_PORT = 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andy:Access@localhost/school'

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Mbuguack@localhost/watchlist_test'

    pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    
    '''
   
    # SQLALCHEMY_DATABASE_URI = ""
    



Class TestConfig(config):
    #SQLALCHEMY_DATABASE_URI = ''

class DevConfig(Config):
  
    #SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}