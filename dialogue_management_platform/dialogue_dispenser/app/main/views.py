# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        views.py
# @time:        2020/8/3 8:34 下午

"""
Notes:...
"""

from . import disperser
from flask import request, jsonify
from app.handlers.gate import Gate_of_data


@disperser.route("/answer", methods=["POST"])
def disperse():
    # 接收对话窗口信息，必须字段为用户id为前端传递的模版号
    uid = "robot_" + request.form.get("uid")        # 用户id
    template_id = request.form.get("template_id")         # 模版号，query时==-1
    query = request.form.get("query")               # 文字性问题
    click_data = request.form.get("click_data")     # 按钮点选的json数据

    Gate_of_data.set_data(uid, template_id, query, click_data)
    result = Gate_of_data.get_data(uid)

    return jsonify(result)
