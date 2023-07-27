import requests
import datetime
import smtplib
import time

MY_LAT = 40.575565
MY_LONG = -111.838162
MY_EMAIL = "welch.charlie16@gmail.com"



def is_overhead():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()

    data = res.json()["iss_position"]
    long = float(data["longitude"])
    lat = float(data["latitude"])

    if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LONG - 5 <= long <= MY_LONG + 5:
        return True


def is_night():
    params = {"lat": MY_LAT, "long": MY_LONG, "formatted": 0}

    res = requests.get("https://api.sunrise-sunset.org/json", params=params)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    curr_time = datetime.now()

    if curr_time >= sunset or curr_time <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg:"Subject: Look Up!\n\nThe ISS is above you in the sky"
        )
