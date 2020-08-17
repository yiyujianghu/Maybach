# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        base_handler.py
# @time:        2020/8/10 5:11 下午

"""
Notes:...
"""

from abc import ABCMeta, abstractmethod


class BaseHandler(metaclass=ABCMeta):
    """
    所有handler的初始化方法，必须传递这四个参数，实现归一化
    def __init__(self, uid, template, query, click_data):
        pass
    """

    @abstractmethod
    def run(self):
        """所有handler处理问题的函数，必须实现以完成工厂模式与多态映射"""
        pass


""" ***** 第二部分 ***** """
scene_mapping_table = {
    "查询天气":{
        "routing_key":"weather",
        "slot_list":["datetime"],
    },
    "预订餐馆":{
        "routing_key": "restaurant",
        "slot_list": ["datetime", "people", "money"],
    },
    "预订酒店":{
        "routing_key": "hotel",
        "slot_list": ["datetime", "people", "money"],
    }
}


""" ***** 第三部分 ***** """
from .query_handler import QueryHandler
from .click_handler import ClickHandler

template_dict = {
    "-1": QueryHandler,
    "1": ClickHandler,
}


""" ***** 第四部分 ***** """
"""
本来打算将redis的读写放到生产者中，但本着尽量解耦的逻辑，在生产者中应使代码尽量与具体的业务逻辑无关，只处理向意图分发的过程；
其他处理都扔到消费者中完成，并且消费者应该与生产者同步目前的场景名称及路由key；
"""

from datetime import datetime
from app.connections import redis_client


class SessionInitial(object):
    @classmethod
    def redis_init(cls, uid):
        now_time = datetime.now()
        time_str = datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        session_dcit = {
            "create_time": time_str,
            "intent": "其他",
        }
        redis_client.dialogue_data_initial(uid, session_dcit)
