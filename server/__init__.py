# -*- coding:utf-8 -*-
# $File: __init__.py
# $Author: cz <chenze-321n[at]163[dot]com>

"""
    website entrance
"""

_app = None
_db = None

def get_app():
    """ Load flask config, initial app and return application"""
    import os
    from flask import Flask
    from flask_login import LoginManager
    from common.config import app_config

    global get_app, _app
    get_app = lambda: _app # avoid duplicate import

    this_file = os.path.realpath(__file__)
    cur_dir = os.path.dirname(this_file)
    par_dir = os.path.dirname(cur_dir)
    static_folder = os.path.join(par_dir, 'static')
    template_folder = os.path.join(par_dir, 'templates')

    _app = Flask(__name__,
                 static_folder=static_folder,
                 static_url_path='',
                 template_folder=template_folder)


    _app.debug = True
    _app.config.from_object(app_config)
    _app.secret_key = "if this is not setted, login will raise exception"

    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(userId):
        from model import User
        user = User.get_user(userId)
        if user is not None:
            user._authenticated=True
        return user

    return _app

def get_db():
    global get_db, _db
    get_db = lambda: _db # avoid duplicate import
    import sqlite3
    
    from common.config import db_config
    _db = sqlite3.connect(db_config.DB_PATH)
    
    app = get_app()
    @app.teardown_appcontext
    def close_connect(exception):
        if _db is not None:
            _db.close()
    
    return _db

get_db()
