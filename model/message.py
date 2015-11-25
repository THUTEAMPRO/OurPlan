# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db

GROUP_INVITE_TYPE = 1
GROUP_JOIN_REQUEST_TYPE = 2
VOTE_VOTING = 3
TASK_ADD = 5


_db=get_db()
class Message(_db.Model):
    __tablename__ = 'message'
    id = _db.Column(_db.Integer, primary_key=True)
    groupid = _db.Column(_db.String(128), index=True)
    messageType = _db.Column(_db.Integer)

    def __init__(self):
        pass
        
    def __repr__(self):
        return '<Message %r>' % self.groupid

    def get_dict(self):
        return dict(id=self.id,\
            info=self.info)
