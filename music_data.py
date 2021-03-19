import spotipy
import yaml
from spotipy.oauth2 import SpotifyOAuth

with open("spotify/client_details.yml", 'r') as stream:
    client_details = yaml.safe_load(stream)

scope = "user-library-read user-follow-read user-top-read playlist-read-private playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_details['client_id'],
    client_secret=client_details['client_secret'],
    redirect_uri=client_details['redirect_uri'],
    scope=scope,
))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

playlists = sp.current_user_playlists()

playlist_items = sp.playlist_items('')