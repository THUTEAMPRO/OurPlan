# -*- coding:utf-8 -*-
# $File: login.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *

    
class AddVoteForm(Form):
    groupid = IntegerField('groupid', validators=[Required()])
    title = StringField('title', validators=[Required()])
    info = StringField('info')
    options = StringField('options')

    def validate_options(self, field):
        return ;
        raise ValidationError('not implements.')


@api_impl("/add_vote",methods=["POST","GET"])
def add_vote(**kwargs):
    form = AddVoteForm(csrf_enabled=False);
    if form.validate_on_submit():
        task_username = current_user.username
        if form.groupid.data is not None:
            task_username = "_group_" + str(form.groupid.data)
        task_tmp = Task(username=task_username,\
                            date=form.date.data, time=form.time.data,\
                            title=form.title.data, info=form.info.data)
        db.session.add(task_tmp)
        db.session.commit()
        return dict(success=1,id=task_tmp.id,title=task_tmp.title)
    else:
        return dict(fail=1)

@api_impl("/user_get_vote",methods=["POST","GET"])
def add_vote(**kwargs):
    return dict()
    

    
@api_impl("/do_vote/<int:voteid>/<int:optionid>",methods=["POST","GET"])
def do_vote(**kwargs):
    return dict()
