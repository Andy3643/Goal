from . import db
from flask import Usermixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
import pytz

date_time=datetime.utcnow().replace(tzinfo=pytz.UTC)
time_zone=date_time.astimezone(pytz.timezone('Africa/Nairobi'))


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


class Pitch(db.Model):
    __tablename__='pitch'
    id=db.Column(db.Integer,primary_key=True)
    pitch=db.Column(db.String())
    pitch_category=db.Column(db.String(20))
    posted=db.Column(db.DateTime,default=time_zone)
    upvotes=db.Column(db.Integer)
    downvotes=db.Column(db.Integer)
    comment=db.relationship('Comment',backref='pitch',lazy='dynamic')
    user_id=db.Column(db.Integer,db.ForeignKey('users.id')) 
    

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))


    def __repr__(self):
        return f"Comment ('{self.comment}','{self.user}')"
        
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comment=Comment.query.filter_by(pitch_id=pitch_id).all()
        return comment



