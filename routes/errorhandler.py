# -*- coding:utf-8 -*-
# $File: errorhandler.py
# $Author: cz <chenze-321n[at]163[dot]com>
from util import *


@app.errorhandler(404)
def needhelp(error):
    return render_template("404.html"), 404
