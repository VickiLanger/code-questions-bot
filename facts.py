'''
facts.py: some facts for @CodeQBot
3 April 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

# TODO: add more facts
# NOTE: please add  fact, then comment the source/reference


fact = [
    # 'fact goes here',  # reference
    'The first Apple computer was made using old parts they collected from their staff for free.',  #
    'The first mouse was made out of wood.',  #
    'Grace Hopper recorded (taped) the first computer ‘bug’, a moth, in the book as she was working for the MARK II computer.',  # https://www.nationalgeographic.org/thisday/sep9/worlds-first-computer-bug/
    'In 1961, the IBM 7094 became the first computer to sing, singing the song Daisy Bell.',  #
    'The language "C" got it\'s name because it succeeded the language "B".',  #
    'JavaScript\'s design was influenced by AWK, C, HyperTalk, Java, Lua, Perl, Python, Scheme, and Self',  #
    'Java was initially designed with the primary aim for use in Interactive television.',  #
    'https://twitter.com/CodeQBot/status/1222986645563232256',  #
    ]

facts = list(str('Did you know \n' + choice(fact) + '\n'))
