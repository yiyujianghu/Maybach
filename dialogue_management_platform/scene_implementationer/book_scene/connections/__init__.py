# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        __init__.py.py
# @time:        2020/8/6 4:01 下午

"""
Notes:...
"""

from .redis_connection import RedisConnection
from .rabbitmq_connection import RabbitmqConnection
from config import DataBaseConfig

redis_client = RedisConnection(
    host=DataBaseConfig.REDIS_HOST,
    port=DataBaseConfig.REDIS_PORT,
    db=DataBaseConfig.REDIS_DB,
    password=DataBaseConfig.REDIS_PASSWORD,
    decode_responses=DataBaseConfig.REDIS_DECODE_RESPONSES,
    expired_in_seconds=DataBaseConfig.REDIS_EXPIRED_IN_SECONDS,
)

rabbitmq_client = RabbitmqConnection(
    host=DataBaseConfig.RABBIT_HOST,
    port=DataBaseConfig.RABBIT_PORT,
    username=DataBaseConfig.RABBIT_USERNAME,
    password=DataBaseConfig.RABBIT_PASSWORD,
    heartbeat=0
)

__all__ = ["redis_client", "rabbitmq_client"]
