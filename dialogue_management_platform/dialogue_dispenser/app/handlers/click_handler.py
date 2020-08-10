# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        click_handler.py
# @time:        2020/8/10 5:09 下午

"""
Notes:...
"""

from .base_handler import BaseHandler, scene_mapping_table
from app.models import NLU
from app.connections import rabbitmq_client

class ClickHandler(BaseHandler):
    def __init__(self, uid, query, click_data):
        self._uid = uid
        self._query = query
        self._click_data = click_data

    def run(self):
        pass
