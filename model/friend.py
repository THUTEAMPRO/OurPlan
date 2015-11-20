# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
import user

_db=get_db()
class Friend(_db.Model):
    __tablename__ = 'friends'
    id = _db.Column(_db.Integer, primary_key=True)
    userid = _db.Column(_db.Integer, index=True)
    friendid = _db.Column(_db.Integer, index=True)
    def __init__(self,userid,friendid):
        self.userid = userid
        self.friendid = friendid
        
    def __repr__(self):
        return '<Friend %r %r>' % (self.userid, self.friendid)
    
    def get_dict(self):
        return dict();
