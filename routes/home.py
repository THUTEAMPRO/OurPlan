# -*- coding:utf-8 -*-
# $File: home.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.route("/")
@app.route("/home")
def home():
    return render_template("example.html", content="args example")
