'''
questions.py: questions to be used by tweet.py for @CodeQBot
21 January 2020
Vicki Langer (@vicki_langer)
'''

from questions_acronyms import acronym_questions
from questions_back_end import back_end_questions
from questions_front_end import front_end_questions
from questions_history import history_questions
from questions_http_statuses import http_status_questions
from questions_misc import misc_questions
from questions_personal import personal_questions
from questions_pop_culture import pop_culture_questions
from questions_version_control import version_control_questions


# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

QUESTIONS = acronym_questions + back_end_questions + front_end_questions + http_status_questions + history_questions + http_status_questions + misc_questions + personal_questions + pop_culture_questions + version_control_questions
