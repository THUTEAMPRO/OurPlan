# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *
import uuid


@app.route("/")
@app.route("/home")
def home():
    api.message.read_message()
    user_data={}
    task_data=[]
    group_data=[]
    group_task_data={}
    all_message=[]
    put_uuid=str(uuid.uuid1())
    if current_user.is_authenticated:
        user_data=current_user.get_dict()
        task_data=api.task.get_task()
        group_data=api.group.user_get_group()
        group_task_data={}
        all_message=api.message.get_message()
        for group in group_data:
            groupid=group["groupid"]
            tasks=api.task.get_group_task(groupid=groupid)
            group_task_data[groupid]=tasks
    if "groupid" in request.args.keys():
        return render_template("example.html", user_data=user_data, task_data=task_data, group_data=group_data, group_task_data=group_task_data,selected_groupid=request.args["groupid"],all_message=all_message,uuid=put_uuid)
    else:
        return render_template("example.html", user_data=user_data, task_data=task_data, group_data=group_data, group_task_data=group_task_data,all_message=all_message,uuid=put_uuid)

@app.route("/share",methods=["POST","GET"])
def share():
    if current_user.is_authenticated:
        api.share.create_temp_task()
    user_data={}
    task_data=[]
    group_data=[]
    group_task_data={}
    if "shareid" in request.args.keys():
        shareid=request.args["shareid"]
        user_data=dict(username="temp")
        task_data=api.share.get_temp_task(tempid=shareid)
    return render_template("share.html", user_data=user_data, task_data=task_data, group_data=[], group_task_data={})

@app.route("/user_edit")
def user_edit():
    return render_template("user_edit.html",all_message=api.message.get_message())


@app.route("/discover")
def discover():
    groups=api.group.all_group()
    return render_template("discover.html",all_message=api.message.get_message(),all_group=groups);

@app.route("/contact")
def contact():
    return render_template("contact.html",all_message=api.get_message());

@app.route("/login")
def _login():
    return redirect('/auth/login')

@app.route("/register")
def _register():
    return redirect('/auth/register')

@app.route("/picker")
def picker():
    return render_template("picker.html");
