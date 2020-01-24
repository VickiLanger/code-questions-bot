'''
get_questions.py: grab a random question
24 January 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from questions import QUESTIONS


def get_question():
    question = choice(QUESTIONS)

    return question
