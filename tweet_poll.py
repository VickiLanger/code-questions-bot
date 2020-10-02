'''
tweet.py: tweet bot to tweet code questions as polls
30 September 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
import requests # to make POST request to send a Poll

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


def main():
    api = authenticate_api()

    account_id="" # required
    pollDurationInMinutes="" # required
    pollQuestion="" # required
    firstChoice="" # required
    secondChoice="" # required
    thirdChoice="" # optional
    fourthChoice="" #optional
    mediaKey="" #optional


    url="https://ads-api.twitter.com/8/accounts/"+account_id+"/cards/poll?duration_in_minutes="+pollDurationInMinutes+"&first_choice="+firstChoice+"&second_choice="+secondChoice+"&third_choice="+thirdChoice+"&fourth_choice="+fourthChoice+"&media_key="+mediaKey+"&name="+pollQuestion

    response=requests.post(url)

    # print(response.text)