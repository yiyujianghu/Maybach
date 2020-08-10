# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        get_data_handler.py
# @time:        2020/8/10 8:13 下午

"""
Notes:...
"""


from app.connections import redis_client, rabbitmq_client


class GetDataHandler(object):
    def __init__(self, uid):
        self._uid = uid

    def run(self):
        pass
