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

from Spotifysession import Spotifysession

def main():
    
    
    # Define User and Playlist:
    
    user = '1113392617'
    playlist_id = '3nBQnSuVv70nmSNgRtETNJ'
    
    session = Spotifysession(user, playlist_id)
    
    playlist_valence = session.get_features_playlist(feature = 'danceability')


if __name__ == "__main__":
    main()
    