# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Group,GroupRelation
from model import Task, User

"""
 group operation
"""

@api_impl("/user_get_group",methods=["POST","GET"])
@login_required
def user_get_group(**kwargs):
    relations = GroupRelation.query.filter_by(userid=current_user.id).all()
    return map(lambda r:r.get_dict(),relations)

class UpdateGroupForm(Form):
    groupid = IntegerField("GroupId", validators=[Required()])
    jointype = IntegerField("jointype")
    tag = StringField("tags")
    describe = StringField("describe")

@api_impl("/all_group",methods=["POST","GET"])
def all_group(**kwargs):
    groups=Group.query.filter_by().all()
    return map(lambda g:g.get_dict(),groups)
    
@api_impl("/user_update_group",methods=["POST","GET"])
@login_required
def user_update_group(**kwargs):
    form = UpdateGroupForm(csrf_enabled=False);
    if form.validate_on_submit():
        group = Group.query.filter_by(id=form.groupid.data).first();
        if(form.tag.data):
            group.del_all_tag();
            tags = form.tag.data.split(",")
            for tag in tags:
                group.add_tag(tag);
        if(form.jointype.data):
            group.set_jointype(form.jointype.data)
        if(form.describe.data):
            group.describe=form.describe.data
        return dict(success=1)
    else:
        return dict(fail=1)

@api_impl("/id_get_group/<id>",methods=["POST","GET"])
def id_get_group(**kwargs):
    group_tmp = Group.query.filter_by(id=kwargs["id"]).first()
    return group_tmp.get_dict();

class AddGroupForm(Form):
    groupname = StringField("GroupName", validators=[Required()])

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
        

"""
 member operation
"""

@api_impl("/group_get_property/<int:groupid>",methods=["POST","GET"])
@login_required
def group_get_property(**kwargs):
    groupid = kwargs["groupid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        groupDict = group.get_dict()
        for user in groupDict["members"]:
            if user["userid"]==current_user.id:
                groupDict["current_power"]=user["power"]
                break;
        return groupDict;
    else:
        return dict();

@api_impl("/group_get_member/<int:groupid>",methods=["POST","GET"])
@login_required
def group_get_member(**kwargs):
    groupid = kwargs["groupid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        return group.get_member()
    else:
        return []
    
    
@api_impl("/group_add_member/<int:groupid>/<int:userid>",methods=["POST","GET"])
@login_required
def group_add_member(**kwargs):
    groupid = kwargs["groupid"]
    userid = kwargs["userid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        group.add_member(userid)
        return dict(success=1)
    else:
        return dict(fail=1)

@api_impl("/group_allow_member/<int:groupid>/<int:userid>",methods=["POST","GET"])
@login_required
def group_allow_member(**kwargs):
    groupid = kwargs["groupid"]
    userid = kwargs["userid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        group.allow_member(userid)
        return dict(success=1)
    else:
        return dict(fail=1)

@api_impl("/group_del_member/<int:groupid>/<int:userid>",methods=["POST","GET"])
@login_required
def group_del_member(**kwargs):
    groupid = kwargs["groupid"]
    userid = kwargs["userid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        group.del_member(userid)
        return dict(success=1)
    else:
        return dict(fail=1)

@api_impl("/group_exit/<int:groupid>",methods=["POST","GET"])
@login_required
def group_exit(**kwargs):
    print "dosth"
    groupid = kwargs["groupid"]
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        group.del_member(current_user.id);
        return dict(success=1);
    else:
        return dict(fail=1)

@api_impl("/group_join/<int:groupid>",methods=["POST","GET"])
@login_required
def group_join(**kwargs):
    groupid = kwargs["groupid"]
    userid = current_user.id
    group = Group.query.filter_by(id=groupid).first()
    if group is not None:
        group.join_member(userid)
        return dict(success=1)
    else:
        return dict(fail=1)
