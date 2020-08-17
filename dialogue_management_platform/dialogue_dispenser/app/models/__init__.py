# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        __init__.py.py
# @time:        2020/8/6 9:21 下午

"""
Notes:...
"""

from .intent_recognition import IntentRecognition
from sinan import Sinan


class NLU(object):
    @classmethod
    def nlu_parse(cls, query):
        intent = IntentRecognition.recognise_intent(query)
        si = Sinan(query)
        slots = si.parse()
        return {"intent":intent, "slots":slots}


if __name__ == "__main__":
    result = NLU.nlu_parse("预订明天上午的两人桌菜")
    print(result)