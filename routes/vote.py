# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *



@app.route("/vote", methods=["POST","GET"])
def vote():
    re=api.vote.add_vote()
    print "vote result:",re
    group_data=api.group.user_get_group()
    vote_data=api.vote.user_get_vote()
    vote_undo_data=api.vote.user_get_undo_vote()
    return render_template("vote.html", group_data=group_data,vote_data=vote_data,vote_undo_data=vote_undo_data);
