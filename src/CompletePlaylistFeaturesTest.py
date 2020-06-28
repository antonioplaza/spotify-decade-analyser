#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:31:02 2020

@author: antonioplaza
"""

# This file saves the features from all the tracks.

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import json


# Obtain client ID and Secret Key. 

def get_keys():
   "Function that reads the client key and the secret key from a Json file."
   with open('credentials.json', 'r') as f:
    credentials = json.load(f)
   return credentials


def get_Spotify_session():
    "Get credentials, authentificate and returns spotify session"
    
    # Obtain credentials to authenthicate.
    credentials = get_keys()

    # Access to Spotify:
    client_credentials_manager = SpotifyClientCredentials(credentials["client_id"], credentials["client_secret"]) 
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
    sp.trace=False

    return sp


# Obtains Uris of all the songs in a playlist (max 100)

def get_song_ids_from_playlist(user, playlist, sp):
    "Function that returns the IDs from all the songs of the playlist."
    playlist = sp.user_playlist(user, playlist_code, fields="tracks,next")
    songs = playlist["tracks"] ["items"]    
    playlist_uris = [uris['track']['id'] for uris in songs]
    return playlist_uris


# Obtains features of uris:
    
def get_features_of_uris(uris, sp):
    "Function that returns the features from all the uris."
    song_valence = sp.audio_features(uris)[100]['valence']
    return song_valence


# Start Spotify Session:

sp = get_Spotify_session()

# Define User and Playlist:

user = '1113392617'
playlist = '3nBQnSuVv70nmSNgRtETNJ'

# Get the uirs from playlist:

playlist_songs = get_song_ids_from_playlist(user, playlist, sp)
uris = get_song_ids_from_playlist(user, playlist)




# Access to Sunday Morning (2nd song of the playlist):

sunday_morning = songs[1]
sunday_morning_info = sunday_morning["track"]
sunday_morning_uri = sunday_morning_info["uri"]

# Access to song features:

sunday_morning_features = sp.audio_features(tracks=[sunday_morning_uri])[0]

uri_list = [features['track']['id'] for features in songs]


playlist_features = sp.audio_features(tracks=[sunday_morning_uri])


# Get IDs o URIS from Playlist.
