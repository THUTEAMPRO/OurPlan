# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db

_db=get_db()
class Group(_db.Model):
    __tablename__ = 'tasks'
    id = _db.Column(_db.Integer, primary_key=True)
    groupname = _db.Column(_db.String(128), index=True)
    username = _db.Column(_db.String(128), index=True)

    def __init__(self, groupname, username):
        self.username = username
        self.groupname = groupname


    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Group %r>' % self.groupname
