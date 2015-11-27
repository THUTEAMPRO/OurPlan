# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *
from model import Vote, Task
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
    voteid=kwargs["voteid"]
    optionid=kwargs["optionid"]
    vote=Vote.query.filter_by(id=voteid).first();
    if(vote.check_user_done(current_user.id)):
        return dict(fail=1)
    option=vote.do_vote(current_user.id,optionid)
    if(option is not None):
        datetime=option.option_datetime
        task_username = "_group_" + str(vote.groupid)
        task_tmp = Task(username=task_username,\
                            date=datetime, time=datetime,\
                            title=vote.title, info=vote.info)
        db.session.add(task_tmp)
        db.session.commit()
        return dict(success=1)
    else:
        return dict(success=1)
    return dict(fail=1)

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
    

@api_impl("/user_get_undo_vote",methods=["POST","GET"])
@login_required
def user_get_undo_vote(**kwargs):
    relations = GroupRelation.query.filter_by(userid=current_user.id).all()
    voteJson = []
    for relation in relations:
        votes = Vote.query.filter_by(groupid=relation.groupid).all()
        for vote in votes:
            if (not vote.finished) and (not vote.check_user_done(current_user.id)):
                voteJson.append(vote.get_dict())
    return voteJson

@api_impl("/all_vote",methods=["POST","GET"])
def get_all_vote(**kwargs):
    votes = Vote.query.filter_by().all()
    return map(lambda vote:vote.get_dict(),votes)
    
