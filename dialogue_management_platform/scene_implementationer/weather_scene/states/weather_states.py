# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        weather_states.py
# @time:        2020/8/14 3:39 下午

"""
Notes:...
"""

from base_component import BaseState, BaseStrategy, BaseProcess


class InitState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def run(self):
        pass


class ClarifyState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def run(self):
        pass


class AnswerState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def run(self):
        pass

