# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Task

class AddTaskForm(Form):
    date = DateTimeField('Date')
    time = DateTimeField('Time')
    info = StringField("String")
    title = StringField("String")

@api_impl("/add_task",methods=["POST","GET"])
@login_required
def add_task(**kwargs):
	return dict(dosth=321)

@api_impl("/del_task",methods=["POST","GET"])
@login_required
def del_task(**kwargs):
	return dict(dosth=321)

@api_impl("/update_task",methods=["POST","GET"])
@login_required
def update_task(**kwargs):
	return dict(dosth=321)

@api_impl("/read_task",methods=["POST","GET"])
@login_required
def read_task(**kwargs):
	return dict(dosth=321)
