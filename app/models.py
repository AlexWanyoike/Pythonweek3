from datetime import datetime
from . import db , login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    description = db.Column(db.String(), index = True)
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)


    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'


class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"


class Like (db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer,primary_key=True)
    like = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_likes(self):
        db.session.add(self)
        db.session.commit()

    def add_likes(cls,id):
        like_pitch = Like(user = current_user, pitch_id=id)
        like_pitch.save_likes()
    
    @classmethod
    def get_likes(cls,id):
        like = Like.query.filter_by(pitch_id=id).all()
        return like

    @classmethod
    def get_all_likes(cls,pitch_id):
        likes = Like.query.order_by('-id').all()
        return likes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Dislike (db.Model):
    __tablename__ = 'dislikes'

    id = db.Column(db.Integer,primary_key=True)
    dislike = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_dislikes(self):
        db.session.add(self)
        db.session.commit()

    def add_dislikes(cls,id):
        dislike_pitch = Dislike(user = current_user, pitch_id=id)
        dislike_pitch.save_dislikes()

    @classmethod
    def get_dislikes(cls,id):
        dislike = Dislike.query.filter_by(pitch_id=id).all()
        return dislike


    @classmethod
    def get_all_dislikes(cls,pitch_id):
        dislikes = Dislike.query.order_by('-id').all()
        return dislikes


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
