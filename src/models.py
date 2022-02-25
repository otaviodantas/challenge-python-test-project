import re
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List


@dataclass
class PriceBook:
    weekday_regular: float
    weekday_reward: float
    weekend_regular: float
    weekend_reward: float

    def regular_client_price(self, is_weekend: bool):
        if is_weekend:
            return self.weekend_regular
        return self.weekday_regular

    def rewards_client_price(self, is_weekend: bool):
        if is_weekend:
            return self.weekend_reward
        return self.weekday_reward


@dataclass
class Budget:
    name: str
    total_price: float
    rank: int


class ClientType(Enum):
    REGULAR = 'regular'
    REWARD = 'rewards'


@dataclass
class InputHandler:
    origin_string: str
    client_type: ClientType = field(default=None)
    date_list: List[int] = field(default=None)

    def __post_init__(self):
        try:
            client_type = self.__search_pattern("\w*:")
            date_list = self.__search_pattern("\([a-zA-Z0-9]*\)")
            self.client_type = ClientType(client_type[0].strip(':').lower()).value
            self.date_list = self.__transform_in_datetime(
                [date.strip("(").strip(")").capitalize()[:3] for date in date_list]
            )
        except Exception as err:
            raise err

    def __search_pattern(self, pattern) -> List[str]:
        return re.findall(pattern, self.origin_string)

    @staticmethod
    def __transform_in_datetime(date_list: List[str]) -> List[int]:
        weekdays = {
            "Mon": 0,
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
            "Fri": 4,
            "Sat": 5,
            "Sun": 6,
        }
        days = []
        for date in date_list:
            days.append(weekdays[date])

        return days
