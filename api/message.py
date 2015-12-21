# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from flask_login import current_user
from model import Message
    
"""
"""

@api_impl("/get_message",methods=["POST","GET"])
@login_required
def get_message(**kwargs):
    allMessages = Message.query.filter_by(userid=current_user.id).all();
    return map(lambda m:m.get_dict(),allMessages)


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

