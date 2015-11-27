# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User
from flask import session
from auth.forms import LoginForm, RegistrationForm
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
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        username = form.username.data
        emails = form.email.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None:
            db = get_db()
            user_tmp = User(username=username, email=emails)
            user_tmp.password=password
            db.session.add(user_tmp)
            db.session.commit()
            login_user(user_tmp)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = username
        session['email'] = emails
        return dict(success=1)
    else:
        return dict(fail=1)
