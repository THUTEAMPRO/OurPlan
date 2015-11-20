# -*- coding:utf-8 -*-
# $File: __init__.py
# $Author: cz <chenze-321n[at]163[dot]com>

from user import User
from task import Task
from group import Group, GroupRelation

from server import get_db

_db = get_db()
_db.create_all()
