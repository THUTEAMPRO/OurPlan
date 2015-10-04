#!.env/bin/python
# -*- coding:utf-8 -*-
# $File: start.py
# $Author: cz <chenze-321n[at]163[dot]com>
from server import get_app

"""
def wsgi_app():
    app=get_app()
    import routes
    return app
"""

def main():
    app=get_app()
    import routes
    import api
    app.run(app.config['HOST'],
            app.config['PORT'],
            **app.config['OPTIONS'])

if __name__=='__main__':
    main()
