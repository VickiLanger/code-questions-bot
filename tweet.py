'''
tweet.py: tweet bot to tweet code quetions
21 January 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
from time import sleep

from os import environ

import get_question

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main():
    print("I'm working, kinda")
    # interval = 60 * 60 * 6  # seconds * minutes * hours
    interval = 30  # every 30 seconds, for testing purposes
    while True:
        print("finding a question...")
        question = get_question()
        api.update_status(question)
        print('question has been tweeted')
        time.sleep(interval)


main()
