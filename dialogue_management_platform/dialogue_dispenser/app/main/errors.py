# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        errors.py
# @time:        2020/8/6 8:55 下午

"""
Notes:...
"""

from . import disperser
from flask import jsonify

@disperser.errorhandler(404)
def not_found_error(error):
    return jsonify({"error":"URL未识别", "info":"fail"}), 404


@disperser.errorhandler(500)
def internal_error(error):
    # 处理数据库事务回滚等操作
    return jsonify({"error":"服务器内部错误", "info":"fail"}), 500
