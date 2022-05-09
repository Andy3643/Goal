#create brains for the app
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    
    
    
    
    
    db.init_app(app)
    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app