# -*- coding:utf-8 -*-
# $File: __init__.py
# $Author: cz <chenze-321n[at]163[dot]com>

from user import User, UserTag
from task import Task
from group import Group, GroupRelation, GroupTag
from friend import Friend
from vote import Vote
from message import Message

from server import get_db

_db = get_db()
_db.create_all()
