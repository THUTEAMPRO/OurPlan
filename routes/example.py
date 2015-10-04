# -*- coding:utf-8 -*-
# $File: example.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.route("/example")
def example():
    """ example for get method """
    return "args: "+str(request.args)

@app.route("/example/<test>")
def example_url(test):
    """ example for url args """
    return "args: "+str(test)

@app.route("/example_post", methods=["POST"])
def example_post():
    """ examle for post method """
    return "data:("+request.data+")"+"form:("+str(request.form)+")"

@app.route("/example_render")
def example_render():
    """ examle for jinja2 render """
    return render_template("example.html",content="args example")

