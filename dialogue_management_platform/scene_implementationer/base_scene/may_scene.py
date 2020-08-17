# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        may_scene.py
# @time:        2020/8/13 8:35 下午

"""
Notes:...
"""

import json
from connections import rabbitmq_client
from base_component import BaseProcess


def task_process(ch, method, properties, body):
    # =============== 以下是信息获取的阶段 ===============
    uid = method.routing_key.split(".")[-1]
    message = json.loads(body)
    intent = message.get("intent")
    slots = message.get("slots")

    # =============== 以下是任务执行的阶段 ===============
    if uid not in task_pool:
        task_pool[uid] = BaseProcess(uid)

    task_pool[uid].turn()


if __name__ == "__main__":
    print("场景服务已启动，正在接收生产者分发的消息...")
    task_pool = {}
    rabbitmq_client.receive_topic_message("query", ["other.*"], task_process)
