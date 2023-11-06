import os
import json
import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"
TEQUILA_API_KEY = os.environ['API_KEY']

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_codes = []

    def get_iata_codes(self, city_names):
        print("[INFO] - Get IATA codes triggered")

        header = {
            'apikey': TEQUILA_API_KEY,
        }

        for city in city_names:
            query = {'term': city, 'location_types': 'city'}
            res = requests.get(f"{TEQUILA_ENDPOINT}locations/query", headers=header, params=query)
            res = res.json()['locations']
            code = res[0]['code']
            print(code)
            self.city_codes.append(code)

        return self.city_codes
    
    def get_prices(self, origin_city_code, destination_city_code, from_time, to_time):
        print(f"[INFO] - Check flights triggered for {destination_city_code}")
        header = {
            'apikey': TEQUILA_API_KEY
        }

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime('%d/%m/%Y'),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        res = requests.get(f"{TEQUILA_ENDPOINT}v2/search", headers=header, params=query)

        try:
            data = res.json()['data'][0]
        except IndexError:
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data