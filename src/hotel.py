from typing import List

from src.models import PriceBook, Budget


class Hotel:
    weekdays = list(range(0, 5))
    weekend = list(range(5, 7))

    def __init__(self, name: str, ranking: int, price_book: PriceBook):
        self.name = name
        self.ranking = ranking
        self.price_book = price_book

    def sum_of_prices(self, date: List[int], client_type: str) -> Budget:
        """
        Receives list of data and return the sum of prices
        :param date: list of data
        :example: [0, 1, 2]
        :param client_type: type of client
        :example: 'regular' or 'rewards'
        """
        if client_type == 'regular':
            all_price = [
                self.price_book.regular_client_price(self._is_weekend(d)) for d in date
            ]
            price = sum(all_price)
        else:
            all_price = [
                self.price_book.rewards_client_price(self._is_weekend(d)) for d in date
            ]
            price = sum(all_price)

        return Budget(name=self.name, total_price=price, rank=self.ranking)

    def _is_weekend(self, date: int) -> bool:
        if date in self.weekdays:
            return False
        return True
