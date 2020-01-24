'''
tweet.py: tweet bot to tweet code quetions
21 January 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
import time

from os import environ

from get_question import get_question

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    interval = 60 * 60 * 6  # seconds * minutes * hours
    while True:
        print("finding a question...")
        question = get_question()
        print("chose question: " + question)
        api.update_status(question)
        print('question has been tweeted')
        time.sleep(interval)


main()
