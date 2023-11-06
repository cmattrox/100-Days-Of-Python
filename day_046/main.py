import requests
import os
import spotipy
from bs4 import BeautifulSoup
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify",
        redirect_uri="http://example.com",
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

########################### Get top 100 songs ###########################
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
web_page = res.text
soup = BeautifulSoup(web_page, "html.parser")
songs_list = soup.find_all(class_="o-chart-results-list-row-container")

########################### Create spotify playlist ###########################
playlist_id = sp.user_playlist_create(user_id, f"{date} Billboard 100")["id"]

########################### Create list of song URIs ###########################
songs = []
for song in songs_list:
    song_name = song.select_one("h3")
    song_artist = song_name.find_next_sibling()

    query = f"track%3A{song_name.getText().strip()}%2520artist%3A{song_artist.getText().strip()}"

    spotify_res = sp.search(query, limit=1, type="track")

    songs.append(spotify_res["tracks"]["items"][0]["uri"])

########################### Add list of songs to playlist ###########################
sp.playlist_add_items(playlist_id, songs)
