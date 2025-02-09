import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIFY_ID'),
    client_secret=os.getenv('SPOTIFY_SECRET'),
    redirect_uri="http://localhost:8080/callback",
    scope="playlist-modify-private",  
    show_dialog=True,
    cache_path="token.txt"
))


year = input("Which year do you want to travel to? Type the date in this format  YYYY-MM-DD: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/", headers=header)
web = response.text

soup = BeautifulSoup(web, 'html.parser')
title_of_songs = soup.select('li ul li h3')
songs = [song.getText().strip() for song in title_of_songs]

user_id = sp.me()["id"]

play_list = sp.user_playlist_create(user_id, f"Billboard Top 100-{year}", public=False, collaborative=False,description="Welcome to time travel machine")

song_uris = []
for song in songs:
    song = sp.search(q=f"name: {song}: {year[0:4]}", limit=1, type='track')
    try:
        song_uris.append(song["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f'Track number {songs.index(song) + 1} could not be found')    

sp.playlist_add_items(playlist_id=play_list["id"], items=song_uris)        
print(f"\n...Your playlist has been created, we managed to find a total of {len(song_uris)}/100 of the top 100 songs! ")
