# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
    
"""
"""

@api_impl("/find_group_by_tag/<string:tag>",methods=["POST","GET"])
@login_required
def find_group_by_tag(**kwargs):
    return dict()

@api_impl("/find_user_by_tag/<string:tag>",methods=["POST","GET"])
@login_required
def find_user_by_tag(**kwargs):
    return dict()

