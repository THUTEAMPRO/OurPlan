# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Group,GroupRelation
from model import Task

    
"""
 group operation
"""

@api_impl("/user_get_group",methods=["POST","GET"])
@login_required
def user_get_group(**kwargs):
    relations = GroupRelation.query.filter_by(userid=current_user.id).all()
    return map(lambda r:r.get_dict(),relations)


@api_impl("/id_get_group/<id>",methods=["POST","GET"])
def id_get_group(**kwargs):
    group_tmp = Group.query.filter_by(id=kwargs["id"]).first()
    return group_tmp.get_dict();

class AddGroupForm(Form):
    groupname = StringField("GroupName")
    

@api_impl("/add_group",methods=["POST","GET"])
@login_required
def add_group(**kwargs):
    form = AddGroupForm(csrf_enabled=False);
    if form.validate_on_submit():
        group_tmp = Group(userid=current_user.id,\
                              groupname=form.groupname.data)
        db.session.add(group_tmp)
        db.session.commit()
        group_tmp.bind();
        reDict=group_tmp.get_dict();
        reDict["success"]=1;
        return reDict
    else:
        return dict(fail=1)
        
class DelGroupForm(Form):
    id = IntegerField("GroupId", validators=[Required()])

@api_impl("/del_group",methods=["POST","GET"])
@login_required
def del_group(**kwargs):
    form = DelTaskForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_tmp = Task.query.filter_by(id=form.id.data).first()
        db.session.delete(task_tmp)
        return dict(success=1)
    else:
        return dict(fail=1)

"""
 member operation
"""
    
class UpdateTaskForm(Form):
    id = IntegerField("Info", validators=[Required()])
    date = DateTimeField('Date', format="%Y-%m-%d")
    time = DateTimeField('Time', format="%H:%M:%S")
    info = StringField("Info")
    title = StringField("Title")

@api_impl("/add_member",methods=["POST","GET"])
@login_required
def add_member(**kwargs):
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

@api_impl("/del_member",methods=["POST","GET"])
@login_required
def del_member(**kwargs):
    return dict(map(lambda t:(t.id,t.get_dict()), Task.query.filter_by(username=current_user.username).all()))

