#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

music = {'danceability': 0.428,
 'energy': 0.365,
 'key': 4,
 'loudness': -11.889,
 'mode': 0,
 'speechiness': 0.0276,
 'acousticness': 0.78,
 'instrumentalness': 0.0033,
 'liveness': 0.113,
 'valence': 0.236,
 'tempo': 94.033,
 'type': 'audio_features',
 'id': '0C6dSPCqwKqwos6s1CrDrh',
 'uri': 'spotify:track:0C6dSPCqwKqwos6s1CrDrh',
 'track_href': 'https://api.spotify.com/v1/tracks/0C6dSPCqwKqwos6s1CrDrh',
 'analysis_url': 'https://api.spotify.com/v1/audio-analysis/0C6dSPCqwKqwos6s1CrDrh',
 'duration_ms': 198554,
 'time_signature': 3,
 'name': 'The Car',
 'album': 'The Car',
 'year': '2022-10-21'}

response = requests.post(url, json=music).json()
print(response)
