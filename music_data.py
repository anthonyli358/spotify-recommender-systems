import spotipy
import yaml
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from data_functions import offset_api_limit, get_artists_df, get_tracks_df, get_track_audio_df,\
    get_all_playlist_tracks_df, get_recommendations


with open("spotify/spotify_details.yml", 'r') as stream:
    spotify_details = yaml.safe_load(stream)

scope = "user-library-read user-follow-read user-top-read playlist-read-private playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_details['client_id'],
    client_secret=spotify_details['client_secret'],
    redirect_uri=spotify_details['redirect_uri'],
    scope=scope,
))

# Spotify API calls and data manipulation
# print("Getting, transforming, and saving top artist data...")
# top_artists = offset_api_limit(sp, sp.current_user_top_artists())
# top_artists_df = get_artists_df(top_artists)
# top_artists_df.to_pickle("spotify/top_artists.pkl")
#
# print("Getting, transforming, and saving followed artist data...")
# followed_artists = offset_api_limit(sp, sp.current_user_followed_artists())
# followed_artists_df = get_artists_df(followed_artists)
# followed_artists_df.to_pickle("spotify/followed_artists.pkl")
#
# print("Getting, transforming, and saving top track data...")
# top_tracks = offset_api_limit(sp, sp.current_user_top_tracks())
# top_tracks_df = get_tracks_df(top_tracks)
# top_tracks_df = get_track_audio_df(sp, top_tracks_df)
# top_tracks_df.to_pickle("spotify/top_tracks.pkl")
#
# print("Getting, transforming, and saving saved track data...")
# saved_tracks = offset_api_limit(sp, sp.current_user_saved_tracks())
# saved_tracks_df = get_tracks_df(saved_tracks)
# saved_tracks_df = get_track_audio_df(sp, saved_tracks_df)
# saved_tracks_df.to_pickle("spotify/saved_tracks.pkl")
#
# print("Getting, transforming, and saving playlist track data...")
# playlist_tracks_df = get_all_playlist_tracks_df(sp, sp.current_user_playlists())
# playlist_tracks_df = get_track_audio_df(sp, playlist_tracks_df)
# playlist_tracks_df.to_pickle("spotify/playlist_tracks.pkl")

print("Getting, transforming, and saving tracks recommendations...")
playlist_tracks_df = pd.read_pickle("spotify/playlist_tracks.pkl")
recommendation_tracks = get_recommendations(sp, playlist_tracks_df[playlist_tracks_df
                                                                   ['playlist_name'] == 'Chill']['id'].tolist())
recommendation_tracks_df = get_tracks_df(recommendation_tracks)
recommendation_tracks_df = get_track_audio_df(sp, recommendation_tracks_df)
recommendation_tracks_df.to_pickle("spotify/recommendation_tracks.pkl")
