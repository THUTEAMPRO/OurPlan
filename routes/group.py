# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *



@app.route("/group",methods=["POST","GET"])
def group():
    api.group.user_update_group();
    group_data=api.group.user_get_group()
    return render_template("group.html", group_data=group_data,all_message=api.message.get_message());
