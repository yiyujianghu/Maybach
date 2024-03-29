# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        query_handler.py
# @time:        2020/8/10 5:08 下午

"""
Notes:...
"""

import json
from .base_handler import BaseHandler, scene_mapping_table
from app.models import NLU
from app.connections import rabbitmq_client, redis_client


class QueryHandler(BaseHandler):
    def __init__(self, uid, query, click_data):
        self._uid = uid
        self._query = query
        self._click_data = click_data

    def run(self):
        message = NLU.nlu_parse(self._query)
        print("nlu message: {}".format(message))
        intent = message.get("intent")
        pre_intent = redis_client.get_dialogue_data(self._uid, "intent")
        if intent != "其他":
            current_intent = intent
        elif pre_intent != "其他":
            current_intent = pre_intent
        else:
            current_intent = "其他"

        redis_client.set_dialogue_data(self._uid, "intent", current_intent)
        print("intent:{}, pre_intent:{}, curr_intent:{}".format(intent, pre_intent, current_intent))

        routing_key = ".".join([scene_mapping_table.get(current_intent, {"routing_key":"other"}).get("routing_key"), self._uid])
        print("routing_key: {}".format(routing_key))
        message.update({"uid":self._uid})
        message_to_send = json.dumps(message)
        rabbitmq_client.send_topic_message("query", routing_key, message_to_send)
