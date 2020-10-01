'''
get_questions.py: grab a random question
24 January 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from questions import QUESTIONS


def get_question():
    # Reads asked questions from file and makes a list of them
    with open("./questions_dir/asked_questions.txt",'r',encoding="utf-8") as f:
        asked_questions = set(f.read().split('``'))
    asked_questions.remove('')
    # If the list is as big as our questions to ask, then all questions have been asked so clear the file and the list
    if len(asked_questions) == len(set(QUESTIONS)):
        asked_questions = set()
        with open('./questions_dir/asked_questions.txt','w', encoding="utf-8") as f:
            f.write('')
    # Ask a questions that hasn't been asked
    question_to_tweet = choice(list(set(QUESTIONS)-asked_questions))
    # Add the asked question to the file
    with open("./questions_dir/asked_questions.txt",'a', encoding="utf-8") as f:
        q = question_to_tweet+"``"
        f.write(q)
    return question_to_tweet