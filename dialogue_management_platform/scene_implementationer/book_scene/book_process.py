# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        book_process.py
# @time:        2020/8/17 2:53 下午

"""
Notes:...
"""


from states.book_state import InitState, ClarifyState, AnswerState
from base_component import BaseProcess
from connections import redis_client

class BookProcess(BaseProcess):
    def __init__(self, uid):
        super().__init__(uid)
        self.intent = None
        self.slots = None

        self.clarify_state = ClarifyState(self)
        self.answer_state = AnswerState(self)
        self.current_state = self.clarify_state

    def drive(self):
        pass

    def set_intent(self, intent):
        self.intent = intent
        if not redis_client._redis_client.hexists(self.uid, intent):
            redis_client.set_dialogue_data(self.uid, self.intent, {
                "datetime":"",
                "people": "",
                "money": ""
            })

    def set_slots(self, slots):
        content = redis_client.get_dialogue_data(self.uid, self.intent)
        print("book content:{}".format(content))
        for k, v in content.items():
            if k in slots:
                content[k] = slots[k][0]
            else:
                pass
        redis_client.set_dialogue_data(self.uid, self.intent, content)

    def turn(self):
        self.current_state = self.current_state.select_state()
        self.current_state.run()
