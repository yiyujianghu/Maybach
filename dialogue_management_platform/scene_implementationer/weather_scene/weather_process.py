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
from connections import redis_client


class WeatherProcess(BaseProcess):
    def __init__(self, uid):
        super().__init__(uid)
        print("有无key", redis_client._redis_client.hexists(self.uid, "weather"))
        if not redis_client._redis_client.hexists(self.uid, "weather"):
            redis_client.set_dialogue_data(uid, "weather", {"datetime":""})

        self.clarify_state = ClarifyState(self)
        self.answer_state = AnswerState(self)
        self.current_state = self.clarify_state

    def set_slots(self, slots):
        content = redis_client.get_dialogue_data(self.uid, "weather")
        print("weather content:{}".format(content))
        for k, v in content.items():
            if k in slots:
                content[k] = slots[k][0]
            else:
                pass
        redis_client.set_dialogue_data(self.uid, "weather", content)

    def drive(self):
        pass

    def turn(self):
        self.current_state = self.current_state.select_state()
        self.current_state.run()


