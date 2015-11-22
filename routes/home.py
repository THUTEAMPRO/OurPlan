# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.route("/")
@app.route("/home")
def home():
    user_data={}
    task_data=[]
    group_data=[]
    group_task_data={}
    if current_user.is_authenticated:
        user_data=current_user.get_dict()
        task_data=api.task.get_task()
        group_data=api.group.user_get_group()
        group_task_data={}
        for group in group_data:
            groupid=group["groupid"]
            tasks=api.task.get_group_task(groupid=groupid)
            group_task_data[groupid]=tasks
    return render_template("example.html", user_data=user_data, task_data=task_data, group_data=group_data, group_task_data=group_task_data)

@app.route("/group")
def group():
    group_data=api.group.user_get_group()
    return render_template("group.html", group_data=group_data);

@app.route("/user_edit")
def user_edit():
    return render_template("user_edit.html")

@app.route("/vote")
def vote():
    group_data=api.group.user_get_group()
    return render_template("vote.html", group_data=group_data);

@app.route("/discover")
def discover():
    return render_template("discover.html");

@app.route("/contact")
def contact():
    return render_template("contact.html");

@app.route("/login")
def _login():
    return redirect('/auth/login')

@app.route("/register")
def _register():
    return redirect('/auth/register')

@app.route("/picker")
def picker():
    return render_template("picker.html");
