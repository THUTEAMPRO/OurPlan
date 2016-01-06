# -*- coding:utf-8 -*-
# $File: user.py
# $Author: cz <chenze-321n[at]163[dot]com>


from server import get_db
from user import User

POWER_TEMP=-1
POWER_CREATER=1
POWER_MANAGER=2
POWER_MEMBER=3

GROUP_JOIN_INVITE=1
GROUP_JOIN_ALLOW=2
GROUP_JOIN_FREE=3

_db=get_db()
class Group(_db.Model):
    __tablename__ = 'groups'
    id = _db.Column(_db.Integer, primary_key=True)
    groupname = _db.Column(_db.String(128), index=True)
    createrid = _db.Column(_db.Integer)
    jointype = _db.Column(_db.Integer)
    describe = _db.Column(_db.String(1024))
    def __init__(self,userid,groupname):
        self.createrid = userid
        self.groupname = groupname
        self.jointype = GROUP_JOIN_FREE
        
    def __repr__(self):
        return '<Group %r>' % self.groupname
    
    def bind(self):
        relation = GroupRelation(self.createrid,self.id,POWER_CREATER)
        _db.session.add(relation)
        _db.session.commit()

    def set_jointype(self, jointype):
        if(jointype>=1 and jointype<=3):
            self.jointype = jointype;

    def join_member(self,userid):
        if self.jointype==GROUP_JOIN_ALLOW:
            self.add_member(userid,POWER_TEMP)
        else:
            self.add_member(userid,POWER_MEMBER)

    def allow_member(self, userid):
        relation = GroupRelation.query.filter_by(groupid=self.id,userid=userid).first()
        if(relation is not None):
            relation.power=POWER_MEMBER
            _db.session.commit()

    def add_member(self, userid, power=POWER_MEMBER):
        relation = GroupRelation.query.filter_by(groupid=self.id,userid=userid).first()
        if(relation is not None):
            return ;
        else:
            relation = GroupRelation(userid, self.id, power)
            _db.session.add(relation)
            _db.session.commit()
            
    def del_tag(self, tag):
        groupTag = GroupTag.query.filter_by(groupid=self.id,tag=tag).first()
        if(groupTag is not None):
            _db.session.delete(groupTag)
            _db.session.commit()
        else:
            return ;
    def del_all_tag(self):
        groupTag = GroupTag.query.filter_by(groupid=self.id).all()
        for tag in groupTag:
            _db.session.delete(tag)
        _db.session.commit()
        
    def get_tag(self):
        groupTags = GroupTag.query.filter_by(groupid=self.id).all()
        if groupTags is not None:
            return map(lambda t:t.tag,groupTags);
        else:
            return []
    
    def add_tag(self, tag):
        groupTag = GroupTag.query.filter_by(groupid=self.id,tag=tag).first()
        if(groupTag is not None):
            return ;
        else:
            groupTag = GroupTag(self.id,tag);
            _db.session.add(groupTag)
            _db.session.commit()
            return ;

    def del_member(self, userid):
        relation = GroupRelation.query.filter_by(groupid=self.id,userid=userid).first()
        if(relation is not None):
            if relation.power!=POWER_CREATER:
                _db.session.delete(relation)
                _db.session.commit()
                
    def get_member(self):
        relations = GroupRelation.query.filter_by(groupid=self.id).all()
        userRelations = map(lambda r:User.query.filter_by(id=r.userid).first(),r, relations)
        userJson= []
        for u,r in userRelations:
            if((u is not None) and r.power!=POWER_TEMP):
                userJson.append(dict(username=u.username,userid=u.id))
        return userJson
                
    def get_dict(self):
        relations = GroupRelation.query.filter_by(groupid=self.id).all()
        userJson= []
        tempJson= []
        for r in relations:
            if r.power!=POWER_TEMP:
                u = User.query.filter_by(id=r.userid).first();
                userJson.append(dict(username=u.username,userid=u.id,\
                                    power=r.power))
            else:
                u = User.query.filter_by(id=r.userid).first();
                tempJson.append(dict(username=u.username,userid=u.id,\
                                    power=r.power))
        return dict(id=self.id,\
                        createrid=self.createrid,\
                        groupname=self.groupname,\
                        jointype=self.jointype,\
                        describe=self.describe,\
                        tag=self.get_tag(),\
                        members=userJson,\
                        applyMembers=tempJson)

    @staticmethod
    def get_one(group):
        if type(group)==int:
            return Group.query.filter_by(id=group).first()
        elif type(group)==Group:
            return group
        else:
            return None




        
class GroupTag(_db.Model):
    __tablename__ = 'group_tag'
    id = _db.Column(_db.Integer, primary_key=True)
    groupid = _db.Column(_db.Integer, index=True)
    groupname = _db.Column(_db.String(128))
    tag = _db.Column(_db.String(128), index=True)

    def __init__(self, groupid, tag):
        group = Group.get_one(groupid);
        self.tag = tag;
        self.groupid = group.id;
        self.groupname = group.groupname;



    
class GroupRelation(_db.Model):
    __tablename__ = 'user_group'
    id = _db.Column(_db.Integer, primary_key=True)
    userid = _db.Column(_db.Integer, index=True)
    username = _db.Column(_db.String(128))
    groupid = _db.Column(_db.Integer, index=True)
    groupname = _db.Column(_db.String(128))
    power = _db.Column(_db.Integer)

    def __init__(self, userid, groupid, power):
        group = Group.get_one(groupid);
        user = User.get_one(userid)
        self.userid = user.id
        self.username = user.username
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
