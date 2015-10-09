#!.env/bin/python
# -*- coding:utf-8 -*-
# $File: start.py
# $Author: cz <chenze-321n[at]163[dot]com>
from server import get_app
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
def wsgi_app():
    app=get_app()
    import routes
    return app
"""

# enable running from shell for debugging
def manager_main():
    app=get_app()
    manager = Manager(app)
    bootstrap = Bootstrap(app)
    import routes
    import api
    app.run(app.config['HOST'],
            app.config['PORT'],
            **app.config['OPTIONS'])

def main():
    app=get_app()
    import routes
    import api
    app.run(app.config['HOST'],
            app.config['PORT'],
            **app.config['OPTIONS'])

if __name__=='__main__':
  manager_main()  
 # main()
