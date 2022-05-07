#create brains for the app
from flask import Flask
from config import config_options



def create_app(config_name):
    app=Flask(__name__)
    
    
    
    
    
    
    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app