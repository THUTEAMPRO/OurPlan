# -*- coding:utf-8 -*-
# $File: util.py
# $Author: cz <chenze-321n[at]163[dot]com>
from server import get_app
from flask import render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from flask_login import current_user
from model import User
import api
app = get_app()
