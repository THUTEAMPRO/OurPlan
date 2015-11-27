# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User
from flask import session
from auth.forms import LoginForm
from flask_login import current_user

@api_impl("/login", methods=["POST"])
def user_login(**kwargs):
    """ asychronized login api """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return dict(success=1)
        else:
            return dict(fail=1)

@api_impl("/user")
@login_required
def user(**kwargs):
    return dict(success=1,userId=current_user.id)

@api_impl("/register", methods=["POST"])
def user_register(**kwargs):
    form = RegisterationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        #user1 = User.query.filter_by(username=name).first()
        #user2 = User.query.filter_by(email=email).first()
    #if (user1 is None) and (user2 is None):
        db = get_db()
        user_tmp = User(username=username, email=email)
        user_tmp.password = form.password.data
        db.session.add(user_tmp);
        return dict(success=1)
    else:
        return dict(fail=1)
