import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "REPLACE WITH YOUR CLIENT ID"
CLIENT_SECRET = "REPLACE WITH YOUR CLIENT SECRET"
SP = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                                   redirect_uri="https://example.com/callback",
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   show_dialog=True,
                                                   cache_path="token.txt"))

def get_valid_date():
    while True:
        date_str = input("What date do you want to travel to? Enter the date in the format YYYY-MM-DD: ")
        try:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
            continue
        if date > datetime.datetime.now():
            print("You can't travel to the future! Please enter a date in the past or today.")
            continue
        return date_str

def get_song_uris(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    songs = soup.select("li ul li h3")
    songs = [song.getText(strip=True) for song in songs]

    user_id = SP.current_user()["id"]

    song_uris = []
    year = date.split("-")[0]
    for song in songs:
        result = SP.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris, user_id

def create_playlist(date, song_uris, user_id):
    playlist = SP.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    SP.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

if __name__ == "__main__":
   date = get_valid_date()
   song_uris, user_id = get_song_uris(date)
   create_playlist(date, song_uris, user_id)
