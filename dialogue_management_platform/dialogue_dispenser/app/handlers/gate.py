# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        gate.py
# @time:        2020/8/7 3:04 下午

"""
Notes:...
"""

from.base_handler import template_dict, SessionInitial
from .query_handler import QueryHandler
from .click_handler import ClickHandler
from .get_data_handler import GetDataHandler


class Gate_of_data(object):
    @classmethod
    def set_data(cls, uid, template_id, query, click_data, *args, **kwargs):
        SessionInitial.redis_init(uid)
        handler = template_dict.get(template_id)(uid, query, click_data)
        handler.run()

    @classmethod
    def get_data(cls, uid):
        handler = GetDataHandler(uid)
        result = handler.run()
        return result

    @classmethod
    def log_data(cls, uid):
        pass
