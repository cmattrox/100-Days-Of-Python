#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA = "SLC"

data_manager = DataManager()
flight_search = FlightSearch()

# print("Welcome to Charlie's flight club")
# print("We find the best deals and email you")
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# email = input("Please enter your email: ")
# email2 = input("Please re-enter your email: ")

# if email == email2:
#     res = data_manager.post_user(first_name, last_name, email)

#     if res['user']:
#         print("Welcome to the club!")

sheet_data = data_manager.get_data()
for row in sheet_data:
    if row['iataCode'] == '':
        city_names = [row['city'] for row in sheet_data]
        data_manager.city_codes = flight_search.get_iata_codes(city_names)
        data_manager.update_row()
        sheet_data = data_manager.get_data()

destinations = {
    data['iataCode']: {
        "id": data['id'],
        'city': data['city'],
        'price': data['lowestPrice']
    } for data in sheet_data
}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.get_prices(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        pass


