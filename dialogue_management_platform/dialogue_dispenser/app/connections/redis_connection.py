# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        redis_connection.py
# @time:        2020/8/6 4:01 下午

"""
Notes:...
"""

import json
from redis import StrictRedis


class RedisConnection(object):
    _instance = {}

    def __new__(cls, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cls._instance:
            cls._instance[key] = super().__new__(cls)
        return cls._instance[key]

    def __init__(self, host, port, db=0, password="", decode_responses=True, expired_in_seconds=0):
        self._host = host
        self._port = port
        self._db = db
        self._password = password
        self._decode_responses = decode_responses
        self._expired_in_seconds = expired_in_seconds
        self._redis_client = StrictRedis(
            host=self._host,
            port=self._port,
            db=self._db,
            password=self._password,
            decode_responses=self._decode_responses
        )

    def dialogue_data_initial(self, uid, dialogue_data, force_flush=False):
        if force_flush or not self._redis_client.exists(uid):
            self._redis_client.hmset(uid, dialogue_data)
            if self._expired_in_seconds > 0:
                self._redis_client.expire(uid, self._expired_in_seconds)
        else:
            pass

    def set_dialogue_data(self, name, key, value):
        value = json.dumps(value) if isinstance(value, (list, dict)) else value
        self._redis_client.hset(name, key, value)

    def get_dialogue_data(self, name, key):
        result = self._redis_client.hget(name, key)
        try:
            result_load = json.loads(result)
            return result if isinstance(result_load, (int, float)) else result_load
        except:
            return result
