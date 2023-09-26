import requests
import pandas as pd

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "C352ND4UPZ5NY1RJ"
NEWS_API_KEY = "eac87e9b8849495199d2580a097f9ada"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    res = requests.get(
        f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&language=en&sortBy=date&apiKey={NEWS_API_KEY}"
    )

    res.raise_for_status()
    res = res.json()

    print(res['articles'][0]['title'])
    print(res['articles'][1]['title'])
    print(res['articles'][2]['title'])


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
res = requests.get(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=60min&apikey={ALPHA_API_KEY}"
)
res.raise_for_status()
res = res.json()

i = 0
day_1 = ""
day_2 = ""


# for key in res["Time Series (Daily)"]:
#     if i == 0:
#         day_1 = res["Time Series (Daily)"][key]["1. open"]
#     elif i == 1:
#         day_2 = res["Time Series (Daily)"][key]["1. open"]
#     else:
#         break

#     i += 1

curr = 100.00
prev = 110.00

if curr == prev:
    diff = 0
try:
    diff = (abs(curr - prev) / prev) * 100.0
except ZeroDivisionError:
    diff = 0

if diff >= 5 or diff <= -5:
    get_news()



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
