#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:49:22 2020

@author: antonioplaza
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import json

class Spotifysession():
    
    def __init__(self, user, playlist_id): 
        
        self.start_spotify_session()
        self.user = user
        self.playlist_id = playlist_id
        
    
    def get_keys(self):
       "Function that reads the client key and the secret key from a Json file."
       with open('credentials.json', 'r') as f:  # Add paths and add default path.
           credentials = json.load(f)
       return credentials
    

    def start_spotify_session(self):
        "Get credentials, authentificate and returns spotify session"
        
        # Obtain credentials to authenthicate.
        credentials = self.get_keys()
    
        # Access to Spotify:
        client_credentials_manager = SpotifyClientCredentials(credentials["client_id"], credentials["client_secret"]) 
        
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
        self.sp.trace = False
            
    
    def get_song_ids_from_playlist(self):
        "Function that returns the IDs from all the songs of the playlist."
        
        playlist = self.sp.user_playlist(self.user, self.playlist_id, fields="tracks,next")
        songs = playlist["tracks"] ["items"]    
        songs_ids_in_playlist = [uris['track']['id'] for uris in songs]
        
        return songs_ids_in_playlist
    
    
    def get_features_playlist(self, feature = 'valence'):
        "Function that returns the features from all the ids."
        
        songs_ids_in_playlist  = self.get_song_ids_from_playlist()
        playlist_songs_features = self.sp.audio_features(tracks = songs_ids_in_playlist)
        assert feature in playlist_songs_features[0].keys() # This will check if the Feature select exists.
        playlist_songs_certain_feature = [songs[feature] for songs in playlist_songs_features]
        
        return playlist_songs_certain_feature
        


