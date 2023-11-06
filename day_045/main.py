from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
yc_web_page = res.text

soup = BeautifulSoup(yc_web_page, "html.parser")

news_titles = soup.find_all(attrs={"class": "athing"})

for news in news_titles:
    title = news.find(attrs={"class": "titleline"})
    vote_count = news.find(attrs={"class": "votelinks"})
    print(vote_count.center.a)
