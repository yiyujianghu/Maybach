# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        __init__.py.py
# @time:        2020/8/3 8:34 下午

"""
Notes:...
"""

from flask import Blueprint

disperser = Blueprint("main", __name__)

from . import views, errors
