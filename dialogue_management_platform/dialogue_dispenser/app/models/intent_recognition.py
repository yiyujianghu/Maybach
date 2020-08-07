# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        intent_recognition.py
# @time:        2020/8/7 11:45 上午

"""
Notes:...
"""

import re


class IntentRecognition(object):
    """
    简单的用于识别意图的模块。
    预订餐馆：时间、人数、钱数
    预订酒店：时间、人数、钱数
    查询天气：时间
    """

    keywords_dict ={
        "book_before":r"(预约|预订|预定|订|有什么|咨询|问下|问一下)",
        "restaurant":r"(餐馆|餐厅|饭店|饭馆|馆子)",
        "hotel":r"(酒店|房间|宾馆|旅店|客栈|旅社)",
        "weather":r"(天气|气温)",
        "weather_description":r"(热不热|冷不冷|下雨|下雪)"
    }

    rules_dict = {
        r".*{book_before}.*{restaurant}.*".format(**keywords_dict):"预订餐馆",
        r".*{book_before}.*{hotel}.*".format(**keywords_dict):"预订酒店",
        r".*({weather}|{weather_description})".format(**keywords_dict):"查询天气",

    }

    @classmethod
    def recognise_intent(cls, query):
        intent_result = "其他"
        for rule, intent in cls.rules_dict.items():
            if re.search(rule, query):
                intent_result = intent
                break

        return intent_result


if __name__ == "__main__":
    result = IntentRecognition.recognise_intent("明天的天气怎么样")
    print(result)