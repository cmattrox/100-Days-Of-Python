import os
import json
import requests
from pprint import pprint

SHEETS_PRICES_ENDPOINT = os.environ["SHEETS_ENDPOINT"]
SHEETS_USER_ENDPOINT = os.environ["SHEETS_USER_ENDPOINT"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def get_data(self):
        res = requests.get(SHEETS_PRICES_ENDPOINT)
        res = res.json()

        self.data = res["prices"]

        return res["prices"]

    def update_row(self):
        for city in self.data:
            new_data = {"price": {"iataCode": city["iataCode"]}}

        res = requests.put(url=f"{SHEETS_PRICES_ENDPOINT}/{city['id']}", json=new_data)

        print(res.text)

    def post_user(self, first_name, last_name, email):
        input = {
            "user": {"firstName": first_name, "lastName": last_name, "email": email}
        }

        res = requests.post(f"{SHEETS_USER_ENDPOINT}", json=input)

        return json.loads(res.text)
