# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db

#GROUP_INVITE_TYPE = 1
#GROUP_JOIN_REQUEST_TYPE = 2
VOTE_ADD = 1
TASK_ADD = 2


_db=get_db()
class Message(_db.Model):
    __tablename__ = 'message'
    id = _db.Column(_db.Integer, primary_key=True)
    userid = _db.Column(_db.String(128), index=True)
    messageInfo = _db.Column(_db.String(128))
    messageUrl = _db.Column(_db.String(128))
    checked = _db.Column(_db.Boolean)

    def __init__(self,userid,messageInfo,messageUrl):
        self.userid=userid
        self.messageInfo=messageInfo;
        self.messageUrl=messageUrl;
        self.checked=False
        
    def __repr__(self):
        return '<Message %r>' % self.groupid

    def get_dict(self):
        return dict(id=self.id,\
                    messageInfo=self.messageInfo,\
                    messageUrl=self.messageUrl,\
                    checked=self.checked)
