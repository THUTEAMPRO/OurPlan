# -*- coding:utf-8 -*-
# $File: util.py
# $Author: cz <chenze-321n[at]163[dot]com>
from server import get_app
from flask import render_template, request, redirect, Response, url_for
from flask_login import login_user, login_required, logout_user
from flask_login import current_user
import json

import api
app = get_app()

@app.route("/routes")
def show_all_routes():
    url_map = app.url_map;
    reStr=""
    strFormat='\n\t {} -> \n\t\t "{}" \n\t\t {}'
    for rule in url_map.iter_rules():
        methods=filter(lambda x: x in ["POST","GET"],list(rule.methods))
        reStr+=strFormat.format(\
                str(rule.rule),\
                str(rule.endpoint),\
                str(methods))
    return Response(reStr, 200, mimetype='text/plain')
        

# from model import User
