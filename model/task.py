# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db

_db=get_db()
class Task(_db.Model):
    __tablename__ = 'tasks'
    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(128), index=True)
    info = _db.Column(_db.String(128), index=True)
    time = _db.Column(_db.Time, index=True)
    date = _db.Column(_db.Date, index=True)
    datetime = _db.Column(_db.DateTime, index=True)

    def __init__(self, username, date, time):
        self.username = username

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Task %r>' % self.username
