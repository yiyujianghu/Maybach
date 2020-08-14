# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        base_state.py
# @time:        2020/8/13 2:34 下午

"""
Notes:...
"""



class BaseState(object):
    """
    * 对话过程以"场景(scene)"为基本组成单元，而场景又以状态(state)为基本组成单元。
    * 每个状态包含"状态池(next_state_pool)"和"策略池(strategy_pool)"两个组成部分。
        next_state_pool: 下一轮可能状态的集合，在构建场景的时候，先将各个状态初始化完成，然后添加此信息，
                         以使状态跳转仅在有限的轨迹之间完成。
        strategy_pool:  从前一个状态向后一个状态跳转的过程中，遵循策略引导。策略即为一种打分机制，可采取
                        状态机/马尔可夫/深度学习等不同策略。
    * 每个状态包含"驱动(drive)"和"运行(run)"两种方法。
        drive:  驱动是指在该状态下，依据策略池中的策略(单一策略或叠加策略)对下一步可能执行的状态做打分排序，
                然后返回下一轮的状态(类/实例)，必要时会根据一些标志位的逻辑综合判断。
        run:    运行方法则运行该状态下所需要完成的事务，一般来说包括答案查询、话术生成等步骤。
    """

    def __init__(self, process):
        self.processMachine = process
        self.next_state_pool = []

    def run(self):
        raise NotImplementedError
