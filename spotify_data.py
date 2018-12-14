# Written By James Blackledge

# pip install git+https://github.com/plamere/spotipy.git --upgrade
import os, sys, string, random, json, requests, spotipy, spotipy.util as util, webbrowser
from json.decoder import JSONDecodeError

username = sys.argv[1]
clientID = #your_client_id
secretID = #your_secret_id
redirect = 'http://127.0.0.1/'

# py spotify_data.py tn8prqi66zbe8af6kyxqzmecq

try:
    token = util.prompt_for_user_token(username, 'user-read-playback-state', clientID, secretID, redirect)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, 'user-read-playback-state', clientID, secretID, redirect)

spotify = spotipy.Spotify(auth=token)
 
json_data = json.dumps(spotify.current_user_playing_track(), sort_keys=True, indent=4)
current = json.loads(json_data)

playlist_url = current['context']['external_urls']['spotify']
playlist_id = playlist_url.rsplit('/', 1)[-1]

mappings = {
    '37i9dQZF1DWWEJlAGA9gs0': ['1', 'A', 'Classical'],
    '37i9dQZF1DX186v583rmzp': ['2', 'B', 'Rap'],
    '37i9dQZF1DXaXB8fQg7xif': ['3', 'C', 'Electronic']
}

choice = mappings[playlist_id] if playlist_id in mappings else ['4', 'D', 'Other']

with open('./spotify.txt', 'w') as spotify_responses:
    spotify_responses.write(choice[0])

with open('./log.txt', 'a') as log:
    log.write('{0}: {1} ~ {2}\n'.format(sum(1 for _ in open('log.txt')) + 1, choice[1], choice[2]))