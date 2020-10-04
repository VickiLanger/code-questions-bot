'''
tweet.py: tweet bot to tweet code quetions
21 January 2020
Vicki Langer (@vicki_langer)
'''

import tweepy
# import time

from os import environ

from get_question import get_question
from get_reply import get_reply


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
    reply_with = get_reply()

    print("finding a question...")
    question = get_question()
    print("chose question: " + question)
    tweet = api.update_status(question)  # variable used later for reply to this tweet
    print('question has been tweeted')

  
 #   try:
 #      if question:
 #          api.update_status(question)
 #   except tweepy.TweepError as e: #tweepy supports error message as well (https://stackoverflow.com/questions/17157753/get-the-error-code-from-tweepy-exception-instance)
 #       api.update_status(f'I seem to not be working properly.Found {e.response.status} Bug @Vicki_Langer about getting me \
 #                      fixed or help her out by submitting a pull request \
 #                      https://github.com/VickiLanger/code-questions-bot')



    api.update_status(status=reply_with, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    print('chose reply:' + reply_with)
    print('reply has been tweeted')


main()
