# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        __init__.py.py
# @time:        2020/8/3 8:33 下午

"""
Notes:...
"""

import os
from flask import Flask

BASE_DIR = os.path.realpath(os.path.dirname(__file__))


def create_app():
    from .main import disperser as main_blueprint
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app