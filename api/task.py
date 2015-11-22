# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Task

class AddTaskForm(Form):
    date = DateTimeField('Date', format="%Y-%m-%d", validators=[Required()])
    time = DateTimeField('Time', format="%H:%M:%S", validators=[Required()])
    info = StringField("Info")
    title = StringField("Title")
    groupid = IntegerField("GroupId")

@api_impl("/add_task",methods=["POST","GET"])
@login_required
def add_task(**kwargs):
    form = AddTaskForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_username = current_user.username
        if form.groupid.data is not None:
            task_username = "_group_" + str(form.groupid.data)
        task_tmp = Task(username=task_username,\
                            date=form.date.data, time=form.time.data,\
                            title=form.title.data, info=form.info.data)
        db.session.add(task_tmp)
        db.session.commit()
        return dict(success=1,id=task_tmp.id,title=task_tmp.title)
    else:
        return dict(fail=1)
        
class DelTaskForm(Form):
    id = IntegerField("Info", validators=[Required()])

@api_impl("/del_task",methods=["POST","GET"])
@login_required
def del_task(**kwargs):
    form = DelTaskForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_tmp = Task.query.filter_by(id=form.id.data).first()
        db.session.delete(task_tmp)
        return dict(success=1)
    else:
        return dict(fail=1)
    
class UpdateTaskForm(Form):
    id = IntegerField("Info", validators=[Required()])
    date = DateTimeField('Date', format="%Y-%m-%d")
    time = DateTimeField('Time', format="%H:%M:%S")
    info = StringField("Info")
    title = StringField("Title")

@api_impl("/update_task",methods=["POST","GET"])
@login_required
def update_task(**kwargs):
    form = UpdateTaskForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_tmp = Task.query.filter_by(id=form.id.data).first()
        if(task_tmp is not None):
            task_tmp.update(date=form.date.data,\
                                time=form.time.data,\
                                title=form.title.data,\
                                info=form.info.data)
            return dict(success=1)
        else:
            return dict(fail=2)
    else:
        return dict(fail=1)

@api_impl("/get_task",methods=["POST","GET"])
@login_required
def get_task(**kwargs):
    return dict(map(lambda t:(t.id,t.get_dict()), Task.query.filter_by(username=current_user.username).all()))

@api_impl("/get_group_task/<int:groupid>",methods=["POST","GET"])
@login_required
def get_group_task(**kwargs):
    groupid=kwargs.get("groupid")
    if(groupid is not None):
        return dict(map(lambda t:(t.id,t.get_dict()), Task.query.filter_by(username="_group_"+str(groupid)).all()))
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
