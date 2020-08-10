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
from app.connections import rabbitmq_client


class QueryHandler(BaseHandler):
    def __init__(self, uid, query, click_data):
        self._uid = uid
        self._query = query
        self._click_data = click_data

    def run(self):
        message = NLU.nlu_parse(self._query)
        intent = message.get("intent")
        routing_key = scene_mapping_table.get(intent)
        message.update({"uid":self._uid})
        message_to_send = json.dumps(message)
        rabbitmq_client.send_topic_message("query", routing_key, message_to_send)
