from . import db
from flask import Usermixin
from werkzeug.security import generate_password_hash,check_password_hash




class User (Usermixin,db.Model):
    __tablename__ = 'users'
    
    
    id = db.Column(db.Integer,primary_key = True)