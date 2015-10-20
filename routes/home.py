# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.route("/")
@app.route("/home")
def home():
    user=dict(username="testname",password="testpass")
    return render_template("example.html", content="args example", user_data=user, calendar_data={})

@app.route("/login")
def _login():
    return redirect('/auth/login')

@app.route("/register")
def _register():
    return redirect('/auth/register')
