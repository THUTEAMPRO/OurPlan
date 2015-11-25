# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db


_db=get_db()
class Vote(_db.Model):
    __tablename__ = 'vote'
    id = _db.Column(_db.Integer, primary_key=True)
    title = _db.Column(_db.String(128), index=True)
    info = _db.Column(_db.String(128))
    messageType = _db.Column(_db.Integer)
    peopleLimit = _db.Column(_db.Integer)

    def __init__(self):
        pass
        
    def __repr__(self):
        return '<Message %r>' % self.groupid

    def get_dict(self):
        return dict(id=self.id,\
            info=self.info)

class VoteOption(_db.Model):
    __tablename__ = 'vote_option'
    id = _db.Column(_db.Integer, primary_key=True)
    voteid = _db.Column(_db.Integer, index=True)
    option_time = _db.Column(_db.Time, index=True)
    option_date = _db.Column(_db.Date, index=True)
    count = _db.Column(_db.Integer)
    
    def __init__(self):
        pass

    def dosth(self):
        pass

class VoteUser(_db.Model):
    __tablename__ = 'vote_user'
    id = _db.Column(_db.Integer, primary_key=True)
    voteid = _db.Column(_db.Integer, index=True)
    userid = _db.Column(_db.Integer, index=True)

    def __init__(self,userid,voteid):
        self.voteid = voteid
        self.userid = userid
