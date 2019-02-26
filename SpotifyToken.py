import spotipy
import requests
import sys
from spotipy.oauth2 import SpotifyClientCredentials


client_id = r'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # 32 characters
client_secret = r'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # 32 characters
redirect_uri = 'https://example.com/callback'		# random redirect 

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None