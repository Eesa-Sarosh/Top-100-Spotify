from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

clientID = 'YOUR CLIENT ID'
clientSecret = 'YOUR CLIENT SECRET'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=clientID,
        client_secret=clientSecret,
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR USERNAME",
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel? Type your date in YYYY-MM--DD format.")
year = date.split('-')[0]
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
songs = soup.select("li ul li h3")
song_list = [s.getText().strip() for s in songs]
song_uris =[]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlistID = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
print(playlistID)
sp.playlist_add_items(playlist_id=playlistID["id"], items=song_uris)
