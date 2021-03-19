import spotipy
import yaml
from spotipy.oauth2 import SpotifyOAuth
from data_functions import offset_api_limit, get_all_playlist_tracks, get_artists_df, get_tracks_df, get_track_audio_df


with open("spotify/client_details.yml", 'r') as stream:
    client_details = yaml.safe_load(stream)

scope = "user-library-read user-follow-read user-top-read playlist-read-private playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_details['client_id'],
    client_secret=client_details['client_secret'],
    redirect_uri=client_details['redirect_uri'],
    scope=scope,
))

print("Getting top artists...")
top_artists = offset_api_limit(sp, sp.current_user_top_artists())
print("Getting followed artists...")
followed_artists = offset_api_limit(sp, sp.current_user_followed_artists())
print("Getting top tracks...")
top_tracks = offset_api_limit(sp, sp.current_user_top_tracks())
print("Getting saved tracks...")
saved_tracks = offset_api_limit(sp, sp.current_user_saved_tracks())
print("Getting playlist tracks...")
playlist_tracks = get_all_playlist_tracks(sp, sp.current_user_playlists())

# Artist data
print("")
print("Transforming and saving top artist data...")
top_artists_df = get_artists_df(top_artists)
top_artists_df.to_pickle("spotify/top_artists.pkl")

print("Transforming and saving followed artist data...")
followed_artists_df = get_artists_df(followed_artists)
followed_artists_df.to_pickle("spotify/followed_artists.pkl")

# Track data
print("Transforming and saving top track data...")
top_tracks_df = get_tracks_df(top_tracks)
top_tracks_df = get_track_audio_df(sp, top_tracks_df)
top_tracks_df.to_pickle("spotify/top_tracks.pkl")

print("Transforming and saving saved track data...")
saved_tracks_df = get_tracks_df(saved_tracks)
saved_tracks_df = get_track_audio_df(sp, saved_tracks_df)
saved_tracks_df.to_pickle("spotify/saved_tracks.pkl")

print("Transforming and saving playlist track data...")
playlist_tracks_df = get_tracks_df(playlist_tracks)
playlist_tracks_df = get_track_audio_df(sp, playlist_tracks_df)
playlist_tracks_df.to_pickle("spotify/playlist_tracks.pkl")
