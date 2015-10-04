# -*- coding:utf-8 -*-
# $File: api_example.py
# $Author: cz <chenze-321n[at]163[dot]com>

from util import *

@api_impl("/example/<sth>")
def api_example(sth):
    """ example for api get """
    return dict(args=sth)

@api_impl("/example_post",methods=["POST"])
def api_example_post(**kwargs):
    """ example for api post, kwargs is from json.loads """
    return kwargs
