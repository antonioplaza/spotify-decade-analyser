#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:20:41 2020

@author: antonioplaza
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import json


# Obtain client ID and Secret Key. 

def getkeys():
   "Function that reads the client key and the secret key from a Json file."
   with open('credentials.json', 'r') as f:
    credentials = json.load(f)
   return credentials


# Obtain credentials to authenthicate.

credentials = getkeys()

# Access to Spotify:

client_credentials_manager = SpotifyClientCredentials(credentials["client_id"], credentials["client_secret"]) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace=False

# Access to playlist "60s hits" from an spotify user:

user = '1113392617'
playlist_code = '3nBQnSuVv70nmSNgRtETNJ'

playlist = sp.user_playlist(user, playlist_code, fields="tracks,next")
tracks = playlist["tracks"] 
songs = tracks["items"]

# Access to Sunday Morning (2nd song of the playlist):

sunday_morning = songs[1]
sunday_morning_info = sunday_morning["track"]
sunday_morning_uri = sunday_morning_info["uri"]

# Access to song features:

sunday_morning_features = sp.audio_features(tracks=[sunday_morning_uri])[0]

