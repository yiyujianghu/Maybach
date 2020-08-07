# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        database_config.py
# @time:        2020/8/6 4:58 下午

"""
Notes:...
"""


class ReidsConfig:
    """
    redis数据库的配置信息
    """
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = ""
    REDIS_DECODE_RESPONSES = True
    REDIS_EXPIRED_IN_SECONDS = 60 * 60 * 24

class MongoConfig:
    """
    mongodb数据库的配置信息
    """
    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

