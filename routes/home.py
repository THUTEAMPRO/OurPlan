# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.route("/")
@app.route("/home")
def home():
    user_data={}
    task_data=[]
    if current_user.is_authenticated:
        user_data=current_user.get_dict()
        task_data=api.task.get_task()
    return render_template("example.html", user_data=user_data, task_data=task_data)

@app.route("/group")
def group():
    group_data=api.group.user_get_group()
    return render_template("group.html", group_data=group_data);

@app.route("/login")
def _login():
    return redirect('/auth/login')

@app.route("/register")
def _register():
    return redirect('/auth/register')
