# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User, Friend

    
"""
 friend operation
"""

@api_impl("/all_user",methods=["POST","GET"])
def all_user(**kwargs):
    users = User.query.filter_by().all();
    return map(lambda u:u.get_dict(),users);

@api_impl("/find_user/<userinfo>",methods=["POST","GET"])
def find_user(**kwargs):
    userinfo=kwargs["userinfo"];
    if userinfo.find("@")>=0:
        user = User.query.filter_by(email=userinfo).first();
        return [user.get_dict()]
    else:
        if len(userinfo)>=2:
            reUser=[];
            users = all_user();
            for user in users:
                if user["username"].find(userinfo)>=0:
                    reUser.append(user)
            return reUser
        else:
            return [];
