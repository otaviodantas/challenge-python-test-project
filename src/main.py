from src.controller import HotelController
from src.hotel import Hotel
from src.models import PriceBook

if __name__ == '__main__':
    h1 = Hotel(name="Lakewood", ranking=3, price_book=PriceBook(110, 80, 90, 80))
    h2 = Hotel(name="Bridgewood", ranking=4, price_book=PriceBook(160, 110, 60, 50))
    h3 = Hotel(name="Ridgewood", ranking=5, price_book=PriceBook(220, 100, 150, 40))

    hotel_controller = HotelController()
    hotel_controller.add_hotel(h1)
    hotel_controller.add_hotel(h2)
    hotel_controller.add_hotel(h3)

    input1 = "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"
    input2 = "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"
    input3 = "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"

    consult1 = hotel_controller.choice_hotel_by_price(input1)
    consult2 = hotel_controller.choice_hotel_by_price(input2)
    consult3 = hotel_controller.choice_hotel_by_price(input3)

    print(consult1, consult2, consult3)
