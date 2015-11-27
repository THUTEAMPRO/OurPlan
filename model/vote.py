# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
import datetime
from group import Group


_db=get_db()

dtFormat = "%Y-%m-%d %H:%M:%S"

def parseTime(time):
    if(type(time)==str or type(time)==unicode):
        try:
            re = datetime.datetime.strptime(time,dtFormat)
            return re
        except ValueError,e:
            return None
    elif(type(time)==datetime.datetime):
       return time

class Vote(_db.Model):
    __tablename__ = 'vote'
    id = _db.Column(_db.Integer, primary_key=True)
    groupid = _db.Column(_db.Integer, index=True)
    title = _db.Column(_db.String(128), index=True)
    info = _db.Column(_db.String(128))
    limit = _db.Column(_db.Integer)
    finished = _db.Column(_db.Boolean)

    def __init__(self,groupid,title,info,limit):
        self.groupid=groupid
        self.title=title
        self.info=info
        if limit is None:
            self.limit = 2
        else:
            self.limit = limit
        self.finished=False;
        
    def __repr__(self):
        return '<Message %r>' % self.groupid
    
    def check_user_done(self,userid):
        voteUser=VoteUser.query.filter_by(userid=userid,voteid=self.id).first()
        if voteUser is not None:
            return True
        else:
            return False

    def do_vote(self,userid,optionid):
        voteOption=VoteOption.query.filter_by(id=optionid).first()
        voteOption.count=voteOption.count+1;
        voteUser=VoteUser(userid,self.id)
        _db.session.add(voteUser)
        if(voteOption.count>=self.limit):
            self.finished=True
            return voteOption
        else:
            return None

    def set_option(self,optionList):
        print optionList
        for option in optionList:
            time = parseTime(option)
            if time is not None:
                voteOption = VoteOption(self.id,time)
                print voteOption.get_dict()
                _db.session.add(voteOption)
        _db.session.commit()

    def get_option(self):
        return VoteOption.query.filter_by(voteid=self.id).all()

    def get_dict(self):
        group = Group.query.filter_by(id=self.groupid).first()
        optionDict = []
        for option in self.get_option():
            optionDict.append(option.get_dict())

        return dict(id=self.id,\
                    groupname=group.groupname,\
                    groupid=group.id,\
                    options=optionDict,\
                    limit=self.limit,\
                    finished=str(self.finished),\
                    title=self.title,\
                    info=self.info)

class VoteOption(_db.Model):
    __tablename__ = 'vote_option'
    id = _db.Column(_db.Integer, primary_key=True)
    voteid = _db.Column(_db.Integer, index=True)
    option_datetime = _db.Column(_db.DateTime)
    count = _db.Column(_db.Integer)
    
    def __init__(self,voteid,dt):
        self.voteid=voteid
        self.option_datetime=dt
        self.count=0

    def get_dict(self):
        timeStr = self.option_datetime.strftime(dtFormat)
        return dict(id=self.id,\
                    voteid=self.voteid,\
                    option_datetime=timeStr,\
                    count=self.count)

class VoteUser(_db.Model):
    __tablename__ = 'vote_user'
    id = _db.Column(_db.Integer, primary_key=True)
    voteid = _db.Column(_db.Integer, index=True)
    userid = _db.Column(_db.Integer, index=True)

    def __init__(self,userid,voteid):
        self.voteid = voteid
        self.userid = userid
