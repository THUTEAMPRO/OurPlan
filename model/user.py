# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
from werkzeug.security import generate_password_hash, check_password_hash

_db=get_db()
class User(_db.Model):
    __tablename__ = 'users'
    id = _db.Column(_db.Integer, primary_key=True)
    email = _db.Column(_db.String(128), unique=True)
    username = _db.Column(_db.String(128), unique=True, index=True)
    password_hash = _db.Column(_db.String(128), unique=True, index=True)

    @staticmethod
    def get_one(user):
        if type(user)==str:
            return User.query.filter_by(username=user).first()
        elif type(user)==int:
            return User.query.filter_by(id=user).first()
        elif type(user)==User:
            return user
        else:
            return None

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(str(self.password_hash), password)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    def get_dict(self):
        return dict(id=self.id,\
                    username=self.username,\
                    email=self.email)
        
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.username)

class UserTag(_db.Model):
    __tablename__ = 'user_tag'
    id = _db.Column(_db.Integer, primary_key=True)
    userid = _db.Column(_db.Integer, index=True)
    username = _db.Column(_db.String(128), index=True)
    tag = _db.Column(_db.String(128), index=True)

    def __init__(self, userid, tag):
        user = User.get_one(userid);
        self.tag = tag;
        self.userid = user.id;
        self.username = user.username;


