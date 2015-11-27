# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import UserTag, GroupTag, Group
from flask_login import current_user
    
"""
"""

@api_impl("/get_all_tag",methods=["POST","GET"])
def get_all_tag(**kwargs):
    userTags = UserTag.query.distinct(UserTag.tag).all();
    return map(lambda t:t.tag, userTags);



"""
    group_tag operation
"""

@api_impl("/group_get_tag/<int:groupid>",methods=["POST","GET"])
def group_get_tag(**kwargs):
    groupid = kwargs["groupid"]
    allTags = GroupTag.query.filter_by(groupid=groupid).all();
    return map(lambda t:t.tag, allTags)

@api_impl("/group_add_tag/<int:groupid>/<string:tag>",methods=["POST","GET"])
def group_add_tag(**kwargs):
    groupid = kwargs["groupid"]
    tag = kwargs["tag"]
    groupTag = GroupTag.query.filter_by(groupid=groupid,tag=tag).first();
    if userTag is not None:
        return dict(fail=1)
    else:
        groupTag = GroupTag(groupid,tag)
        db.session.add(groupTag)
        return dict(success=1)

    
@api_impl("/group_del_tag/<int:groupid>/<string:tag>",methods=["POST","GET"])
def group_del_tag(**kwargs):
    groupid = kwargs["groupid"]
    tag = kwargs["tag"]
    groupTag = GroupTag.query.filter_by(groupid=groupid,tag=tag).first();
    if userTag is not None:
        db.session.delete(userTag)
        return dict(success=1)
    else:
        return dict(fail=1)


@api_impl("/find_group_by_tag/<string:tag>",methods=["POST","GET"])
def find_group_by_tag(**kwargs):
    tag=kwargs["tag"]
    groupTag = GroupTag.query.filter_by(tag=tag).all();
    groupJsonList=[]
    for tag in groupTag:
        group=Group.query.filter_by(id=tag.groupid).first();
        groupJson=dict(jointype=group.jointype,describe=group.describe,groupname=tag.groupname,groupid=tag.groupid)
        groupJsonList.append(groupJson)
        
    return groupJsonList


"""
    user_tag operation
"""


@api_impl("/user_get_tag",methods=["POST","GET"])
@login_required
def user_get_tag(**kwargs):
    allTags = UserTag.query.filter_by(userid=current_user.id).all();
    return map(lambda t:t.tag,allTags)

@api_impl("/user_add_tag/<string:tag>",methods=["POST","GET"])
@login_required
def user_add_tag(**kwargs):
    tag=kwargs["tag"]
    if tag in user_get_tag():
        return dict(fail=1)
    else:
        userTag = UserTag(current_user.id,kwargs["tag"])
        db.session.add(userTag)
        return dict(success=1);

@api_impl("/user_del_tag/<string:tag>",methods=["POST","GET"])
@login_required
def user_del_tag(**kwargs):
    tag=kwargs["tag"]
    userTag = UserTag.query.filter_by(userid=current_user.id,tag=tag).first();
    if userTag is not None:
        db.session.delete(userTag)
        return dict(success=1)
    else:
        return dict(fail=1)
