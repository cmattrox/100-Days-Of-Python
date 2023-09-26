import requests
from twilio.rest import Client

API_KEY = "25c74abc651baafb187feac2db59b611"
ACCOUNT_SID = "AC9e9a5110d4c63baba613e9e88768710d"
AUTH_TOKEN = "0586763f57b5432de824a89651e763ac"
lat = 40.569710
lon = -111.897278

res = requests.get(
    f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=imperial&appid={API_KEY}"
)
res.raise_for_status()
res = res.json()

today = res["daily"][0]
summary = today["summary"]
temp_max = today["temp"]["max"]
temp_min = today["temp"]["min"]

message = f"Today's Weather:\n{summary}\nHigh: {temp_max}\nLow: {temp_min}"

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(from_="+18335450507", to="+18164623289", body=message)
