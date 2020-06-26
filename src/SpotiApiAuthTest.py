#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:43:41 2020

@author: antonioplaza
"""

# This script tests the connectivity to the application in Spotify.
# It uses Client Credentials Flow instead of Authorization Code Flow.

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

