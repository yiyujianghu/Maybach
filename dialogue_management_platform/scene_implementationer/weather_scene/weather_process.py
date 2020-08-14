# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        weather_process.py
# @time:        2020/8/14 3:52 下午

"""
Notes:...
"""


from states.weather_states import InitState, ClarifyState, AnswerState
from base_component import BaseProcess


class WeatherProcess(BaseProcess):
    def __init__(self, uid):
        super().__init__(uid)

    def drive(self):
        pass

    def run(self):
        pass

