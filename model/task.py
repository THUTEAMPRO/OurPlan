# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db

_db=get_db()
class Task(_db.Model):
    __tablename__ = 'tasks'
    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(128), index=True)
    time = _db.Column(_db.Time, index=True)
    date = _db.Column(_db.Date, index=True)
    title = _db.Column(_db.String(128),index=True)
    info = _db.Column(_db.String(128), index=True)
    duration = _db.Column(_db.Integer)

    def __init__(self, username, date, time, title, info, duration=0):
        self.username = username
        self.time=time.time()
        self.date=date.date()
        self.title=[title, "untitled"][(title is None) or (title=="")]
        self.info=[info, ""][info is None]
        self.duration=duration

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
            self.duration=duration

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Task %r>' % self.username

    def get_dict(self):
        date=self.date
        return dict(id=self.id,\
            username=self.username,\
            time=self.time.strftime("%H:%M:%S"),\
            date="-".join(map(str,[date.year,date.month,date.day])),\
            title=self.title,\
            info=self.info)
