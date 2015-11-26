# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Vote
from model import GroupRelation, Group

    
class AddVoteForm(Form):
    groupid = IntegerField('groupid', validators=[Required()])
    title = StringField('title', validators=[Required()])
    info = StringField('info')
    limit = IntegerField("limit")
    options = StringField('options',validators=[Required()])

@api_impl("/add_vote",methods=["POST","GET"])
@login_required
def add_vote(**kwargs):
    form = AddVoteForm(csrf_enabled=False);
    if form.validate_on_submit():
        userid = current_user.id
        groupid = form.groupid.data
        title = form.title.data
        info = form.info.data
        limit = form.limit.data
        options = form.options.data
        if form.groupid.data is not None:
            vote = Vote(groupid,title,info,limit)
            db.session.add(vote)
            db.session.commit()
            vote.set_option(options.split(","))
            return dict(success=1)
        else:
            return dict(fail=1)
    else:
        return dict(fail=1)

@api_impl("/do_vote/<int:voteid>/<int:optionid>",methods=["POST","GET"])
@login_required
def do_vote(**kwargs):
    return dict()

@api_impl("/do_all_vote",methods=["POST","GET"])
@login_required
def do_all_vote(**kwargs):
    return dict()
    
@api_impl("/user_get_vote",methods=["POST","GET"])
@login_required
def user_get_vote(**kwargs):
    relations = GroupRelation.query.filter_by(userid=current_user.id).all()
    voteJson = []
    for relation in relations:
        votes = Vote.query.filter_by(groupid=relation.groupid).all()
        for vote in votes:
            voteJson.append(vote.get_dict())

    return voteJson
    

@api_impl("/all_vote",methods=["POST","GET"])
def get_all_vote(**kwargs):
    votes = Vote.query.filter_by().all()
    return map(lambda vote:vote.get_dict(),votes)
    
