from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
    
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
   
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  

    def __repr__(self):
        return f'User {self.username}'
    
class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    user = db.Column(db.String(200))
    category = db.Column(db.String(200))
    posted = db.Column(db.DateTime,default = datetime.utcnow)

    def saves_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_pitch_by_category(cls,category):
        pitch_category = Pitch.query.filter_by(category = category)
        
        return pitch_category
    @classmethod
    def get_user_pitch(cls,uname):
        pitch = Pitch.query.filter_by(user = uname).all()
        
        return pitch
    
    @classmethod
    def get_all_pitches(cls):
        pitch_list = Pitch.query.all()
        return pitch_list
    
class Comment(db.Model):
    __tablename__= 'comment'  
    id = db.Column(db.Integer,primary_key = True)
    
    pitch_id = db.Column(db.Integer)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    comment = db.Column(db.String(255))
    user = db.Column(db.String(255))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitch_comment(cls,id):
        comment = Comment.query.filter_by(pitch_id = id)

        return comment
    
    
    
    