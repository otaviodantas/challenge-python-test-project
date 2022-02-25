from unittest import TestCase

from src.models import PriceBook
from src.hotel import Hotel
from src.controller import HotelController


class Integration(TestCase):
    def test_one_hotel(self):
        menager = HotelController()
        h1 = Hotel("One", 3, PriceBook(50, 30, 100, 50))

        menager.add_hotel(h1)

        entry = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        best_hotel = menager.choice_hotel_by_price(entry)

        self.assertEqual(best_hotel, "One")

    def test_two_hotels(self):
        menager = HotelController()
        h1 = Hotel("One", 3, PriceBook(50, 30, 100, 50))
        h2 = Hotel("Two", 2, PriceBook(20, 10, 40, 20))

        menager.add_hotel(h1)
        menager.add_hotel(h2)

        entry = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        best_hotel = menager.choice_hotel_by_price(entry)

        self.assertEqual(best_hotel, "Two")

    def test_three_hotels(self):
        menager = HotelController()
        h1 = Hotel("One", 3, PriceBook(50, 30, 100, 50))
        h2 = Hotel("Two", 2, PriceBook(20, 10, 40, 20))
        h3 = Hotel("Three", 4, PriceBook(100, 50, 200, 70))

        menager.add_hotel(h1)
        menager.add_hotel(h2)
        menager.add_hotel(h3)

        entry = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        best_hotel = menager.choice_hotel_by_price(entry)

        self.assertEqual(best_hotel, "Two")

    def test_two_hotel_with_same_budget(self):
        menager = HotelController()
        h1 = Hotel("One", 5, PriceBook(50, 30, 100, 50))
        h2 = Hotel("Two", 3, PriceBook(50, 30, 100, 50))

        menager.add_hotel(h1)
        menager.add_hotel(h2)

        entry = "Rewards: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
        best_hotel = menager.choice_hotel_by_price(entry)

        self.assertEqual(best_hotel, "One")
