# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from flask_login import current_user
from model import Message
import group
    
"""
"""

@api_impl("/get_message",methods=["POST","GET"])
def get_message(**kwargs):
    if current_user.is_authenticated:
        allMessages = Message.query.filter_by(userid=current_user.id,checked=False).all();
        return map(lambda m:m.get_dict(),allMessages)
    else:
        return [];

def read_message():
    if "messageid" in request.args.keys():
        mid=request.args["messageid"]
        message=Message.query.filter_by(id=mid).first();
        message.checked=True;
    return dict(success=1)

def add_message(**kwargs):
    userid=kwargs["userid"]
    messageInfo=kwargs["messageInfo"]
    messageUrl=kwargs["messageUrl"]
    message_tmp = Message(userid, messageInfo, messageUrl)
    db.session.add(message_tmp)
    db.session.commit()
    return dict(userid=userid,\
                messageInfo=messageInfo,\
                messageUrl=messageUrl)

def group_add_message(**kwargs):
    groupid=kwargs["groupid"]
    members=group.group_get_member(groupid=groupid)
    messageInfo=kwargs["messageInfo"]
    messageUrl=kwargs["messageUrl"]
    for member in members:
        userid=member["userid"]
        message_tmp = Message(userid, messageInfo, messageUrl)
        db.session.add(message_tmp)
    db.session.commit()
    return dict(groupid=groupid,\
                messageInfo=messageInfo,\
                messageUrl=messageUrl)



def vote_add_message(vote):
    messageInfo="新投票:"+vote.info
    messageUrl="/vote?"
    group_add_message(groupid=vote.groupid,\
                      messageInfo=messageInfo,\
                      messageUrl=messageUrl)
    return dict()

def task_add_message(task):
    groupid=task.username[7:]
    messageInfo="新日程:"+task.info
    messageUrl="/home?groupid="+groupid+"&"
    group_add_message(groupid=groupid,\
                      messageInfo=messageInfo,\
                      messageUrl=messageUrl)
    return dict()
