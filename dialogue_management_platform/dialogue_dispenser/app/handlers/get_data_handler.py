# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        get_data_handler.py
# @time:        2020/8/10 8:13 下午

"""
Notes:...
"""


import backoff
from app.connections import redis_client


def _stop_condition(response):
    if response.get("info") == "success":
        return False
    else:
        return True


class GetDataHandler(object):
    def __init__(self, uid):
        self._uid = uid

    @backoff.on_predicate(wait_gen=backoff.fibo, predicate=_stop_condition, max_time=2)
    def run(self):
        answer = redis_client.get_dialogue_data(self._uid, "answer")
        click_list = redis_client.get_dialogue_data(self._uid, "click_list")
        template_id = redis_client.get_dialogue_data(self._uid, "template_id")
        if answer:
            result = {
                "answer":answer,
                "click_list":click_list,
                "template_id":template_id,
                "info": "success"
            }
        else:
            result = {
                "answer": "很抱歉，小May未能理解您的意思，您可以换个说法试试呢～",
                "click_list": [],
                "template_id": -1,
                "info": "no_ack"
            }

        return result

    def clear_answer(self):
        redis_client.hset(self._uid, "answer", "")
        redis_client.hset(self._uid, "click_list", [])
        redis_client.hset(self._uid, "template_id", -1)
