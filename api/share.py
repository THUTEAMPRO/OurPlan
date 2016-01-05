# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Task
import datetime 
import uuid

class CreateTempTaskForm(Form):
    tasklist = StringField("TaskList",validators=[Required()])
    tempid = StringField("uuid", validators=[Required()])

@api_impl("/create_temp_task",methods=["POST","GET"])
@login_required
def create_temp_task(**kwargs):
    form = CreateTempTaskForm(csrf_enabled=False);
    print form.tempid
    if form.validate_on_submit():
        #task_username = current_user.username
        #if form.groupid.data is not None:
            #task_username = "_group_" + str(form.groupid.data)
        tasklist = map(int,form.tasklist.data.split(","))
        tasks=[]
        for taskid in tasklist:
            task=Task.query.filter_by(id=taskid).first()
            if task is not None:
                tasks.append(task)
        tempid=form.tempid.data
        username="_temp_"+tempid
        for task in tasks:
            task_tmp = Task(username=username,\
                            date=task.date,time=task.time,\
                            title=task.title,info=task.info,\
                            duration=task.duration)
            db.session.add(task_tmp)
        db.session.commit()
        return dict(tempid=tempid)
    else:
        return dict(fail=1)


@api_impl("/get_temp_task/<int:tempid>",methods=["POST","GET"])
def get_temp_task(**kwargs):
    tempid=kwargs.get("tempid")
    if(tempid is not None):
        return dict(map(lambda t:(t.id,t.get_dict()), Task.query.filter_by(username="_temp_"+str(tempid)).all()))
    else:
        return dict();


"""
@app.route("/task_test", methods=["POST","GET"])
def task_test():
    form = AddTaskForm();
    if form.validate_on_submit():
        print "yes"
        return render_template("task.html",form=form)
    else:
        return render_template("task.html",form=form)
"""

class TimeTaskForm(Form):
    fromdate = DateTimeField('FromDate', format="%Y-%m-%d")
    todate = DateTimeField('ToDate', format="%Y-%m-%d")
    groupid = IntegerField("GroupId")

@api_impl("/get_time_task",methods=["POST","GET"])
@login_required
def get_time_task(**kwargs):
    form = TimeTaskForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_username = current_user.username
        fromdate=form.fromdate.data;
        todate=form.todate.data;
        fromdate=[fromdate,datetime.date.min][fromdate is None]
        todate=[todate,datetime.date.max][todate is None]
        if form.groupid.data is not None:
            task_username = "_group_" + str(form.groupid.data)
        tasks=Task.query.filter(Task.username==task_username,Task.date>=fromdate,Task.date<=todate).all()
        return dict(map(lambda t:(t.id,t.get_dict()), tasks))
    else:
        return dict(fail=1)

