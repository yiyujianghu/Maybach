# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        weather_states.py
# @time:        2020/8/14 3:39 下午

"""
Notes:...
"""

from base_component import BaseState
from connections import redis_client


class InitState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def select_state(self):
        pass

    def run(self):
        pass


class ClarifyState(BaseState):
    def __init__(self, process):
        super().__init__(process)
        self.slot = None

    def select_state(self):
        content = redis_client.get_dialogue_data(self.uid, "weather")
        for k, v in content.items():
            if not v:
                self.slot = k
                return self.process.clarify_state
            else:
                pass
        return self.process.answer_state

    def run(self):
        clarify_dict = {"datetime":"日期"}
        answer = "请问您想查询的{}是什么呢".format(clarify_dict[self.slot])
        redis_client.set_dialogue_data(self.uid, "answer", answer)


class AnswerState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def select_state(self):
        return self.process.answer_state

    def run(self):
        from datetime import datetime
        now = datetime.now()
        current_time = datetime.strptime("{}-{}-{}".format(now.year, now.month, now.day), "%Y-%m-%d")
        query_time = redis_client.get_dialogue_data(self.uid, "weather").get("datetime").split(" ")[0]
        query_time = datetime.strptime(query_time, "%Y-%m-%d")
        print("current_time:{} query_time:{}".format(current_time, query_time))
        delta_days = (query_time-current_time).days
        print("delta_days:{}".format(delta_days))
        answer_dict = {
            -1: "昨天天气刮起了大风，这些天出门要小心呦～",
            0: "今天天气炎热，请注意做好防暑～",
            1: "明天天气比较舒适，适合外出游玩～",
            2: "后天天气也比较好～"
        }
        answer = answer_dict.get(delta_days, "您问的日期不在天气预报的范围内，请问最近日期的天气～")
        redis_client.set_dialogue_data(self.uid, "answer", answer)


