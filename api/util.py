# -*- coding:utf-8 -*-
# $File: util.py
# $Author: cz <chenze-321n[at]163[dot]com>
from flask import request, Response
from flask_login import login_user, login_required, logout_user, current_user
from functools import wraps
from server import get_app, get_db
#from model import User
import json

app = get_app()
db = get_db()

class api_impl(object):
    api_list = list()

    API_PREFIX = '/api'

    endpoint = ' '

    def __init__(self, url_rule, **kwargs):
        self.url_rule = api_impl.API_PREFIX + url_rule
        self.kwargs=kwargs

    def __call__(self, func):

        func.__doc__ = "Route: {}".format(self.url_rule) + \
                (lambda s:'' if s is None else s)(func.__doc__)

        self.func=func
        self.endpoint = func.__module__ + "." + func.__name__

        @wraps(func)
        def view_func(**kwargs):
            code = 200
            rst = self.func(**kwargs)
            """
            try:
                if(request.method=='POST'):
                    requestArgs = json.loads(request.data)
                    if isinstance(requestArgs, list):
                        raise ValueError("request args can't be list")
                    for k in requestArgs:
                        kwargs[k]=requestArgs[k]
                rst = self.func(**kwargs)
            except ValueError:
                code = 400
                rst = dict(error="request format not right",data=request.data)
            """
            assert isinstance(rst, dict) or isinstance(rst, list),\
                    "ret value {0} can not be jsonified".format(str(rst))

            rst = json.dumps(rst, indent=4)
            resp = Response(rst, code, mimetype='application/json')
            return resp

        app.add_url_rule(self.url_rule, view_func=view_func,
                        endpoint=self.endpoint, **self.kwargs)

        return func

