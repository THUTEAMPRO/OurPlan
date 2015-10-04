# -*- coding:utf-8 -*-
# $File: util.py
# $Author: cz <chenze-321n[at]163[dot]com>
from importlib import import_module
from pkgutil import walk_packages
import os


def import_all_modules(file_path, pkg_name):
    '''
    file_path: dirpath/filename.py
    pkg_name: package name
    import valid ***.py under dirpath as pkg_name.***
    '''
    for _, module_name, _ in walk_packages(
            [os.path.dirname(file_path)], pkg_name + "."):
        mod = import_module(module_name)
