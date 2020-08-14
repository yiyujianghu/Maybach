# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        base_strategy.py
# @time:        2020/8/13 2:50 下午

"""
Notes:...
"""


class BaseStrategy(object):
    """
    * 对话过程中的策略，用于驱动对话运行并得到下一轮对话的状态。
    * 输入：
        (0) 当前状态与下一轮的状态池；---> 策略应当是抽象的，驱动drive才是具体的步骤；
        ======================================================================
        (1) NLU的意图/词槽信息：由生产者传递而来；
        (2) 场景当前信息：例如词槽是否填满，决定澄清话术还是查询答案；一般在redis中；
        (3) 外部数据：例如根据不同用户的不同数据，决定对话走向；
        (4) 标志位：历史对话所产生的一些标志位；
    * 输出：
        对下一轮状态池的各种状态做打分排序。
    """

    def __call__(self, uid, current_state, slots, *args, **kwargs):
        raise NotImplementedError
