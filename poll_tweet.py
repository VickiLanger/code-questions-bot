'''
tweet.py: tweet bot to tweet code questions as polls
30 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy

from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception:
        print(f"An error occurred when attempting to authenticate with the twitter API.")
