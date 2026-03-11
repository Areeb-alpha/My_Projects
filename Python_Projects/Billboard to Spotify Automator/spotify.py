from bs4 import BeautifulSoup
import requests
import spotipy
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

year_input = input("which year do you want to travel to?Type the data in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{year_input}/"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
response = requests.get(URL,headers=header)
music_data = response.text
soup = BeautifulSoup(music_data,"html.parser")

#print(soup.prettify())
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText(strip=True) for song in song_names_spans]
#print(song_names)
REDIRECT_URI = os.environ.get("REDIRECT_URI")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private"
))

# Example: create a playlist in your account
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name="Billboard to spotify", public=False)
playlist_id = playlist["id"]
print("Playlist created:", playlist["external_urls"]["spotify"])

spotify_uris = []
for song in song_names:
    result = sp.search(q=song,type = "track",limit=1)
    tracks = result["tracks"]["items"]
    if tracks:
        uri = tracks[0]["uri"]
        spotify_uris.append(uri)
        print(f"✅ Found: {song} → {uri}")
    else:
        print(f"❌ Not found: {song}")

    # Step 3: Print all collected URIs
print("\nAll Spotify URIs collected:")
for uri in spotify_uris:
      print(uri)

for i in range(0,len(spotify_uris),100):
    sp.playlist_add_items(playlist_id,spotify_uris[i:i+100])
    print(f"Added {len(spotify_uris[i:i+100])} songs to playlist")
