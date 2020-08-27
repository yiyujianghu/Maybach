# -*-conding:utf-8-*-
# Base Information:
# @author:      yiyujianghu
# @project:     <Maybach>
# @file:        book_state.py
# @time:        2020/8/17 2:52 下午

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
        content = redis_client.get_dialogue_data(self.uid, self.process.intent)
        for k, v in content.items():
            if not v:
                self.slot = k
                return self.process.clarify_state
            else:
                pass
        return self.process.answer_state

    def run(self):
        clarify_dict = {
            "datetime":"日期",
            "people":"人数",
            "money":"价格"
        }
        answer = "好的，请问您想查询的{}是什么呢？".format(clarify_dict[self.slot])
        redis_client.set_dialogue_data(self.uid, "answer", answer)


class AnswerState(BaseState):
    def __init__(self, process):
        super().__init__(process)

    def select_state(self):
        return self.process.answer_state

    def run(self):
        from datetime import datetime
        import pandas as pd
        now = datetime.now()
        current_time = datetime.strptime("{}-{}-{}".format(now.year, now.month, now.day), "%Y-%m-%d")
        query_time = redis_client.get_dialogue_data(self.uid, self.process.intent).get("datetime").split(" ")[0]
        query_time = datetime.strptime(query_time, "%Y-%m-%d")
        delta_days = (query_time-current_time).days

        answer_data_restaurant = [
            [0, 3, 75, "望京南吉野家"],
            [0, 5, 400, "凯德Mall南京大排档"],
            [1, 3, 75, "广顺南大街吉野家"],
            [1, 5, 400, "翠微百货南京大排档"],
        ]
        answer_data_hotel = [
            [0, 1, 150, "望京南七天快捷酒店"],
            [0, 2, 800, "广顺南大街豪华酒店"],
            [1, 1, 150, "望京南七天快捷酒店"],
            [1, 2, 800, "广顺南大街豪华酒店"],
        ]
        columns = ["datetime", "people", "money", "answer"]
        answer_df_restaurant = pd.DataFrame(answer_data_restaurant, columns=columns)
        answer_df_hotel = pd.DataFrame(answer_data_hotel, columns=columns)
        answer_df_dict = {
            "restaurant": answer_df_restaurant,
            "hotel": answer_df_hotel,
        }
        people = int(redis_client.get_dialogue_data(self.uid, self.process.intent).get("people")[0])
        money = redis_client.get_dialogue_data(self.uid, self.process.intent).get("money")[0]

        answer_df = answer_df_dict[self.process.intent]
        current_answer_data = answer_df[
                     (answer_df["datetime"] >= delta_days) &
                     (answer_df["people"] >= people) &
                     (answer_df["money"] <= money)
                     ]
        if len(current_answer_data) > 0:
            answer_data_line = current_answer_data.iloc[0, :]
            answer = "已帮您预订日期为{data}，{people}人，价格{money}的{name}~".format(
                data=query_time,
                people=answer_data_line["people"],
                money=answer_data_line["money"],
                name=answer_data_line["answer"]
            )
        else:
            answer = "十分抱歉，未能为您查到相关预订信息！"
        redis_client.set_dialogue_data(self.uid, "answer", answer)

        # 短信发送模块，调用线上SAAS接口
        from twilio.rest import Client

        account_sid = 'AC233dcbe135621ca3bb9edb6d42878083'
        auth_token = "c1c48996403e0575c5a1e859577f2d68"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                             body=answer,
                             from_='+18177674126',
                             to='+8615011086891'
                         )
        print(message.sid)
