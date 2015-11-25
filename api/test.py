# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User, Group
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
        group = Group(userid, "group%s"%i)
        group.describe = "".join([chr(random.choice(range(65,90))) for i in range(10)])
        db.session.add(group)
        db.session.commit()
        groupMap[group.id]=group

    db.session.commit()

    for userid,user in userMap.items():
        group=random.choice(groupMap.values());
        group.add_member(userid)

    for groupid,group in groupMap.items():
        user=random.choice(userMap.values());
        group.add_member(user.id)
            
    return dict();
