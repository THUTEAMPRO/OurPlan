# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
import datetime

def timeParse(sth):
    if type(sth)==datetime.time:
        return sth
    elif type(sth)==datetime.datetime:
        return sth.time()
    else:
        print "time type error"
        return datetime.min().time()

def dateParse(sth):
    if type(sth)==datetime.date:
        return sth
    elif type(sth)==datetime.datetime:
        return sth.date()
    else:
        print "date type error"
        return datetime.min().date()
    
_db=get_db()
class Task(_db.Model):
    __tablename__ = 'tasks'
    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(128), index=True)
    time = _db.Column(_db.Time, index=True)
    date = _db.Column(_db.Date, index=True)
    title = _db.Column(_db.String(128),index=True)
    info = _db.Column(_db.String(128), index=True)
    duration = _db.Column(_db.Time)

    def __init__(self, username, date, time, title, info, duration=0):
        self.username = username
        self.time=timeParse(time)
        self.date=dateParse(date)

        self.title=[title, "untitled"][(title is None) or (title=="")]
        self.info=[info, ""][info is None]
        self.duration=timeParse(duration)

    def update(self, date=None, time=None, title=None, info=None, duration=None):
        if date is not None:
            self.date=date.date()
        if time is not None:
            self.time=time.time()
        if title is not None:
            self.title=title
        if info is not None:
            self.info=info
        if duration is not None:
            self.duration=duration.time()

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Task %r>' % self.username

    def get_dict(self):
        date=self.date
        username=self.username
        if username.find("_group_")>=0:
            return dict(id=self.id,\
                username=self.username,\
                time=self.time.strftime("%H:%M:%S"),\
                date="-".join(map(str,[date.year,date.month,date.day])),\
                title=self.title,\
                info=self.info,\
                groupid=username.replace("_group_",""),\
                duration=self.duration.strftime("%H:%M:%S"))
        else:
            return dict(id=self.id,\
                username=self.username,\
                time=self.time.strftime("%H:%M:%S"),\
                date="-".join(map(str,[date.year,date.month,date.day])),\
                title=self.title,\
                info=self.info,\
                duration=self.duration.strftime("%H:%M:%S"))
