# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        gate.py
# @time:        2020/8/7 3:04 下午

"""
Notes:...
"""

from.base_handler import template_dict
from .query_handler import QueryHandler
from .click_handler import ClickHandler


class Gate_of_data(object):
    @classmethod
    def set_data(cls, uid, template, query, click_data, *args, **kwargs):
        handler = template_dict.get(template)(uid, query, click_data)
        handler.run()

    @classmethod
    def get_data(cls, uid):
        pass

    @classmethod
    def log_data(cls, uid):
        pass
