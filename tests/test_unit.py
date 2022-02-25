from unittest import TestCase

from src.models import InputHandler, ClientType, PriceBook
from src.hotel import Hotel


class Unit(TestCase):
    def test_split_correct_input(self):
        regular_input = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        entry = InputHandler(regular_input)
        self.assertEqual(entry.client_type, ClientType.REGULAR.value)
        self.assertEqual(len(entry.date_list), 3)

    def test_when_input_is_invalid(self):
        invalid_input = "Regular 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        with self.assertRaises(Exception):
            entry = InputHandler(invalid_input)

    def test_date_convert(self):
        regular_input = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        entry = InputHandler(regular_input)
        self.assertEqual(entry.date_list[0], 0)
        self.assertEqual(entry.date_list[1], 1)
        self.assertEqual(entry.date_list[2], 2)

    def test_when_input_is_weekend(self):
        hotel = Hotel("test", 1, PriceBook(1, 3, 4, 5))
        result = hotel._is_weekend(1)
        result2 = hotel._is_weekend(5)
        self.assertEqual(result, False)
        self.assertEqual(result2, True)

    def test_price_to_regular_client(self):
        price = PriceBook(50, 30, 100, 50)
        regular_weekday = price.regular_client_price(False)
        regular_weekend = price.regular_client_price(True)
        reward_weekday = price.rewards_client_price(False)
        reward_weekend = price.rewards_client_price(True)
        self.assertEqual(regular_weekday, 50)
        self.assertEqual(regular_weekend, 100)
        self.assertEqual(reward_weekday, 30)
        self.assertEqual(reward_weekend, 50)
