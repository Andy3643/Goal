from . import db
from flask import Usermixin
from werkzeug.security import generate_password_hash,check_password_hash




class User (Usermixin,db.Model):
    __tablename__ = 'users'
    
    
    id = db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments=db.relationship('Comment',backref='user',lazy='dynamic')
    pitch=db.relationship('Pitch',backref='user',lazy='dynamic')

    password_secure = db.Column(db.String(255))

    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot access the password')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.pitch}')"