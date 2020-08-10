# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        rabbitmq_connection.py
# @time:        2020/8/10 3:02 下午

"""
Notes:...
"""

import pika


class RabbitmqConnection(object):
    """
    这里定义了rabbitmq的初始化与基本的发送/接收方法。
    * 发送方法： 由于要调度不同的队列，且每回的message不同，故而需在业务代码中频繁调用；
    * 接收方法： 理论上将消费者已经确认自己的消费等级，不会频繁更改，故而在进程启动时打开消费即可；
                消费者的callback参数需为一个可调用函数，将接收到匹配message，并在函数中处理：
                def callback(ch, method, properties, body):
                    print("body：{body} 为接收到的信息".format(body))
    """
    _instance = {}

    def __new__(cls, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cls._instance:
            cls._instance[key] = super().__new__(cls)
        return cls._instance[key]

    def __init__(self, host, port, username="", password="", heartbeat=0):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._heartbeat = heartbeat
        self._credential = pika.credentials.PlainCredentials(
            self._username,
            self._password,
        )
        self._connection_parameters = pika.ConnectionParameters(
            host=self._host,
            port=self._port,
            credentials=self._credential,
            heartbeat=self._heartbeat,
        )
        self._connection = pika.BlockingConnection(self._connection_parameters)
        self._channel = self._connection.channel()

    def __del__(self):
        self._connection.close()

    def send_direct_message(self, exchange_name, queue_name, routing_key, message):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        self._channel.queue_declare(queue=queue_name)
        self._channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)
        self._channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=message,
        )

    def receive_direct_message(self, exchange_name, queue_name, routing_key, callback):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        self._channel.queue_declare(queue=queue_name, exclusive=True)
        self._channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)
        self._channel.basic_publish(
            consumer_callback=callback,
            queue=queue_name,
            no_ack=True
        )
        self._channel.start_consuming()

    def send_fanout_message(self, exchange_name, message):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")
        self._channel.basic_publish(
            exchange=exchange_name,
            routing_key="",
            body=message
        )

    def receive_fanout_message(self, exchange_name, callback):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")
        current_queue = self._channel.queue_declare(exclusive=True)
        current_queue_name = current_queue.method.queue
        self._channel.queue_bind(exchange=exchange_name, queue=current_queue_name)
        self._channel.basic_publish(
            consumer_callback=callback,
            queue=current_queue_name,
            no_ack=True
        )
        self._channel.start_consuming()

    def send_topic_message(self, exchange_name, routing_key, message):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type="topic")
        self._channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=message
        )

    def receive_topic_message(self, exchange_name, routing_key_list, callback):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type="topic")
        current_queue = self._channel.queue_declare(exclusive=True)
        current_queue_name = current_queue.method.queue
        for routing_key in routing_key_list:
            self._channel.queue_bind(exchange=exchange_name, queue=current_queue_name, routing_key=routing_key)
        self._channel.basic_consume(
            consumer_callback=callback,
            queue=current_queue_name,
            no_ack=True
        )
        self._channel.start_consuming()
