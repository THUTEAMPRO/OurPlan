# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *

@api_impl("/login/<username>")
def user_login(username):
    """ login api """
    user = User.get_user(username)
    if user is None:
        return dict(error=1)
    else:
        login_user(user)
        return dict(success=1)
