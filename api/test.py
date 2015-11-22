# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User,Group
import random

@api_impl("/fake_db",methods=["GET"])
def fake_db():
    userMap={}
    groupMap={}
    for i in range(10):
        user = User("user%s"%i,"user%s@163.com"%i)
        user.password="test"
        db.session.add(user)
        db.session.commit()
        userMap[user.id]=user;
        
    for i in range(5):
        userid = random.choice(userMap.keys())
        group = Group(userid,"group%s"%i)
        db.session.add(group)
        db.session.commit()
        for t in range(3):
            group.add_member(userid)
            
    return dict();
