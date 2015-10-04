# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>

"""

TODO
need binding with the user information in db

"""
class User(object):
    TEST_USER=None # a simple user for test
    
    @staticmethod
    def get_user(username):
        if(username=="test"):
            if User.TEST_USER is None:
                User.TEST_USER=User();
            return User.TEST_USER
        else:
            return None

    def __init__(self):
        self._authenticated = False

    def is_authenticated(self):
        return self._authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return u"test"
