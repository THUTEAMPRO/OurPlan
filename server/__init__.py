# -*- coding:utf-8 -*-
# $File: __init__.py
# $Author: cz <chenze-321n[at]163[dot]com>

"""
    website entrance
"""
#
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask import Flask
from flask_login import LoginManager
from common.config import app_config
from flask.ext.mail import Mail, Message

_app = None
_db = None
basedir = os.path.abspath(os.path.dirname(__file__))

def get_app():
    """ Load flask config, initial app and return application"""
    global get_app, _app
    get_app = lambda: _app  # avoid duplicate import

    this_file = os.path.realpath(__file__)
    cur_dir = os.path.dirname(this_file)
    par_dir = os.path.dirname(cur_dir)
    static_folder = os.path.join(par_dir, 'static')
    template_folder = os.path.join(par_dir, 'templates')

    _app = Flask(__name__,
                 static_folder=static_folder,
                 static_url_path='',
                 template_folder=template_folder)

    # _app.debug = True
    _app.config['debug'] = True
    _app.config.from_object(app_config)
    _app.secret_key = "if this is not setted, login will raise exception"
    app = Flask(__name__)
    _app.config['SECRET_KEY'] = 'hard to guess string'
    _app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    _app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True



#print 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(userId):
        from model import User

        user = User.get_user(userId)
        if user is not None:
            user._authenticated = True
        return user

    return _app


migrate = Migrate(_app, _db)
_app = get_app()
_db = SQLAlchemy(_app)
def get_db():
    global get_db, _db
  # no effect  _db.create_all()
#
# #
# # get_db = lambda: _db  # avoid duplicate import
# #     import sqlite3
# #
# #     from common.config import db_config
# #
# #     _db = sqlite3.connect(db_config.DB_PATH)


#
#     @app.teardown_appcontext
#     def close_connect(exception):
#         if _db is not None:
#             _db.close()

    return _db



def get_mail():

    import os

    _app.config['MAIL_SERVER'] = 'smtp.qq.com'
    _app.config['MAIL_PORT'] = 25
    _app.config['MAIL_USE_TLS'] = True
    _app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    _app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    _app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
    _app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <huashiyiqike@qq.com>'

#
# def send_email(to, subject, template, **kwargs):
#     msg = Message(_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     mail.send(msg)


get_mail()

#
# class Role(_db.Model):
#     __tablename__ = 'roles'
#     id = _db.Column(_db.Integer, primary_key=True)
#     name = _db.Column(_db.String(64), unique=True)
#     users = _db.relationship('User', backref='role', lazy='dynamic')
#
#     def __repr__(self):
#         return '<Role %r>' % self.name


class User(_db.Model):
    __tablename__ = 'users'
    id = _db.Column(_db.Integer, primary_key=True)
    username = _db.Column(_db.String(64), unique=True, index=True)

    def __init__(self,username):
        self.username = username

    # role_id = _db.Column(_db.Integer, _db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

