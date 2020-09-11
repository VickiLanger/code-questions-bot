'''
get_tweets.py: grab a random question
10 September 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from questions import QUESTIONS


def get_question():
    question_to_tweet = choice(QUESTIONS)

    return question_to_tweet
