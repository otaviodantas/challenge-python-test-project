from src.hotel import Hotel
from src.models import InputHandler


class HotelController:
    def __init__(self):
        self.hotel_list = []

    def add_hotel(self, hotel: Hotel):
        self.hotel_list.append(hotel)

    def choice_hotel_by_price(self, date: str) -> str:
        ranking = []
        checked = self.cast_to_model(date)
        for hotel in self.hotel_list:
            ranking.append(hotel.sum_of_prices(checked.date_list, checked.client_type))

        for i in range(1, len(ranking)):
            key_item = ranking[i]
            j = i - 1
            while j >= 0 and ranking[j].total_price >= key_item.total_price:
                if ranking[j].total_price == key_item.total_price:
                    if ranking[j].rank > key_item.rank:
                        break
                ranking[j + 1] = ranking[j]
                j -= 1
            ranking[j + 1] = key_item

        print([(tier.name, tier.total_price, tier.rank) for tier in ranking])
        return ranking[0].name

    @staticmethod
    def cast_to_model(data) -> InputHandler:
        return InputHandler(data)
