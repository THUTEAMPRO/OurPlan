# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from flask_login import current_user
    
"""
"""

@api_impl("/get_message",methods=["POST","GET"])
@login_required
def get_message(**kwargs):
    return dict()


