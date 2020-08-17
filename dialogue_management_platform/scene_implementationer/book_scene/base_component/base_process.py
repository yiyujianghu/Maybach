# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        base_process.py
# @time:        2020/8/13 5:20 下午

"""
Notes:...
"""


class BaseProcess(object):
    """
    * 对话的场景过程，模拟操作工按流程接待与执行的过程。
    * 过程：
        (1) 首先接待的任务是由生产者分发而来的，故而流程要在消费者中完成运转；
        (2) 消费者分发而来的任务由用户ID识别，故而流程要绑定会话ID；
        (3) 流程的子单元为会话的状态(state)，状态的运转形成流程图，驱动由策略函数指引；
        (4) 根据每个用户ID形成一个流程账本，每回收到用户ID传来的数据，根据策略搜寻然后综合打分，
            然后引导流程向下一节点跳转；
    * 代码层：
        (1) 先用用户ID形成一个场景流程的任务池，即新来一个用户就分配一个流程账本，之后按用户ID查账得到账本地址；
        (2) 根据当前状态、外部输入信息、策略三个方面，判断下一阶段所形成的状态，drive后返回下一阶段状态；
        (3) 根据返回的状态驱动状态的运行run，将话术答案等信息存入该用户ID的redis中，生产者将轮询查询；
        (4) 整体代码封装到外部，然后消费者的callback中调用；
    """
    def __init__(self, uid):
        self.uid = uid
        self.current_state = None
        self.state_pool = []
        self.drive_strategy = None

    def drive(self):
        """ 策略驱动 """
        raise NotImplementedError

    def turn(self):
        """ 机器开动 """
        self.current_state = self.drive()
        self.current_state.run()
        raise NotImplementedError
