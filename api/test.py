# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import User

@api_impl("/test",methods=["POST"])
def test_db(**kwargs):
	print request.POST
	return dict(dosth=321)

