# -*- coding:utf-8 -*-
from flask import Blueprint
from server import get_app


auth = Blueprint('auth', __name__)

from . import views
from . import forms

### register must be put after import 
_app = get_app()
_app.register_blueprint(auth, url_prefix = '/auth')
