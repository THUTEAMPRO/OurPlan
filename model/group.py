# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
import user

POWER_CREATER=1
POWER_MENBER=0

_db=get_db()
class Group(_db.Model):
    __tablename__ = 'groups'
    id = _db.Column(_db.Integer, primary_key=True)
    groupname = _db.Column(_db.String(128), index=True)
    createrid = _db.Column(_db.Integer)
    def __init__(self,userid,groupname):
        self.createrid = userid
        self.groupname = groupname
        
    def __repr__(self):
        return '<Group %r>' % self.groupname
    
    def bind(self):
        relation = GroupRelation(self.createrid,self.id,POWER_CREATER)
        _db.session.add(relation)

    def add_member(self, userid):
        relation = GroupRelation.query.filter_by(groupid=self.id,userid=userid).first()
        if(relation is not None):
            return ;
        else:
            relation = GroupRelation(userid, self.id, POWER_MEMBER)
            _db.session.add(relation)

    def del_member(self, userid):
        relation = GroupRelation.query.filter_by(groupid=self.id,userid=userid).first()
        if(relation is not None):
            if relation.power!=POWER_MEMBER:
                _db.session.delete(relation)
                
    def get_dict(self):
        relations = GroupRelation.query.filter_by(groupid=self.id).all()
        users = map(lambda r:User.query.filter_by(id=r.userid).first(), relations)
        usernames = []
        for u in users:
            if(u is not None):
                usernames.append(u.username)
        return dict(id=self.id,\
                        createrid=self.createrid,\
                        groupname=self.groupname,\
                        members=usernames)
    @staticmethod
    def get_one(group):
        if type(group)==int:
            return Group.query.filter_by(id=group).first()
        elif type(group)==Group:
            return group
        else:
            return None



    
class GroupRelation(_db.Model):
    __tablename__ = 'user_group'
    id = _db.Column(_db.Integer, primary_key=True)
    userid = _db.Column(_db.Integer, index=True)
    groupid = _db.Column(_db.Integer, index=True)
    groupname = _db.Column(_db.String(128))
    power = _db.Column(_db.Integer)

    def __init__(self, userid, groupid, power):
        group = Group.get_one(groupid);
        self.userid = userid
        self.groupid = group.id
        self.groupname = group.groupname
        self.power = power;


    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<GroupRelation %r %r>' % (self.groupid, self.userid)

    def get_dict(self):
        return dict(userid=self.userid,\
                        groupid=self.groupid,\
                        groupname=self.groupname,\
                        power=self.power)
