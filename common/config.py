# -*- coding:utf-8 -*-
# $File: config.py
# $Author: cz <chenze-321n[at]163[dot]com>

class _DefaultConfig(object):
    HOST = "0.0.0.0"
    PORT = 8080
    OPTIONS = {"debug": True,
               "use_reloader": False}
               
app_config = _DefaultConfig()

class _dbConfig(object):
    DB_PATH = ".database.db"
db_config = _dbConfig()
