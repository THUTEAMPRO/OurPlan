#!.env/bin/python
# -*- coding:utf-8 -*-
# $File: start.py
# $Author: cz <chenze-321n[at]163[dot]com>
from server import get_app, get_db
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager, Shell
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
    global app, db, User
    app = get_app()
    app.config['host'] = '0.0.0.0'
    manager = Manager(app)
    from flask.ext.migrate import Migrate, MigrateCommand

    bootstrap = Bootstrap(app)
    db = get_db()
    import routes
    import api

    def make_shell_context():
        return dict(app=app, db=db, User=User)

    manager.add_command("shell", Shell(make_context=make_shell_context))
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)

    manager.run()


def main():
    app = get_app()
    bootstrap = Bootstrap(app)
    import routes
    import api
    #  import pdb;pdb.set_trace();
    app.run(app.config['HOST'],
            app.config['PORT'],
            **app.config['OPTIONS'])


if __name__ == '__main__':
    manager_main()
    # main()
