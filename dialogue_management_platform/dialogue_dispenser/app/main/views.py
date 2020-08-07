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


@disperser.route("/answer", methods=["POST"])
def disperse():
    # 接收对话窗口信息，必须字段为用户id为前端传递的模版号
    uid = "robot_" + request.form.get("cid")        # 用户id
    template = request.form.get("template")         # 模版号，query时==-1
    query = request.form.get("query")               # 文字性问题
    click_data = request.form.get("click_data")     # 按钮点选的json数据

    dialogue_answer = "你好，很高兴为您服务～"
    answer_dict = {
        "answer": dialogue_answer,
        "template_id": -1,
        "click_list": [],
        "info": "success"
    }
    return jsonify(answer_dict)
