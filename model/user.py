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

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

        #     @staticmethod
        #     def get_user(username):
        #         if(username=="test"):
        #             if User.TEST_USER is None:
        #                 User.TEST_USER=User();
        #             return User.TEST_USER
        #         else:
        #             return None
        #
        #     def __init__(self):
        #         self._authenticated = False
        #
        #     def is_authenticated(self):
        #         return self._authenticated
        #
        #     def is_active(self):
        #         return True
        #
        #     def is_anonymous(self):
        #         return True
        #
        #     def get_id(self):
        #         return u"test"
