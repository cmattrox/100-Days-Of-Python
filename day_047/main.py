import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

my_email = "welch.charlie16@gmail.com"
password = "mxapieasxotsyvwe"

URLs = [
    {
        "url": "https://www.amazon.com/WD_BLACK-SN770-Internal-Gaming-Solid/dp/B09QV5KJHV/ref=sr_1_11?crid=24EUZE9JC61FT&keywords=m.2%2Bssd&qid=1699376400&sprefix=m.2%2Bssd%2Caps%2C114&sr=8-11&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&th=1",
        "price": 75.00,
    },
    {
        "url": "https://www.amazon.com/LG-UltraGear-34GP63A-B-Compatibility-FreeSync/dp/B0B928B6BC/ref=sr_1_2?crid=23P9MWNPK5ATC&keywords=curved%2Bgaming%2Bmonitor&qid=1699376685&refinements=p_n_feature_fifteen_browse-bin%3A17751808011%7C17751809011%2Cp_72%3A1248879011%2Cp_89%3AASUS%7CDell%7CLG%7CSAMSUNG%2Cp_n_feature_seventeen_browse-bin%3A17726608011&rnid=6676813011&s=pc&sprefix=curved%2Bgaming%2Bmonitor%2Caps%2C124&sr=1-2&ufe=app_do%3Aamzn1.fos.c3015c4a-46bb-44b9-81a4-dc28e6d374b3&th=1",
        "price": 250.00,
    },
    {
        "url": "https://www.amazon.com/Ninja-DZ201-2-Basket-Technology-Stainless/dp/B089TQWJKK/ref=sr_1_5?crid=S29TO61C3OYX&keywords=airfryer&qid=1699376826&refinements=p_72%3A1248915011&rnid=1248913011&s=home-garden&sprefix=airfryer%2Caps%2C125&sr=1-5&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&th=1",
        "price": 100.00,
    },
]

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
}
for URL in URLs:
    res = requests.get(URL["url"], headers=headers)

    soup = BeautifulSoup(res.text, "lxml")

    price = soup.find_all("span", {"class": "a-offscreen"})[0].getText().strip("$")
    title = soup.find(id="productTitle").get_text().strip()

    message = f"{title} is now less than ${URL['price']}"

    if float(price) < URL["price"]:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL['url']}".encode(
                    "utf-8"
                ),
            )
