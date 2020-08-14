# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        __init__.py.py
# @time:        2020/8/6 4:33 下午

"""
Notes:...
"""

from .database_config import ReidsConfig, MongoConfig, RabbitmqConfig


__all__ = ["DataBaseConfig"]


class DataBaseConfig(ReidsConfig, MongoConfig, RabbitmqConfig):
    """将各种数据库配置的结果打包成一个标准类"""
    def __new__(cls, *args, **kwargs):
        super().__new__(cls)

