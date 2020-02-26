'''
get_reply.py: choose a reply
26 Feb 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

# TODO: add more replies

REPLIES = (
    'Here\'s our question! \nStick around, we\'ll have another in 6 hours! \n\n🤷It may be easy, it may be hard. \n⌨️Either way, give it a tweet \n🔎Don\'t know it? Look it up \n❓Still unsure? Ask',
    'Above is our question! \nCheck back in 6 hours for another! \n\n🤷Maybe it\'s simple, maybe it\'s not \n🖱️Go ahead and tweet \n🧭Not sure? Search the web \n🗺️Still don\'t know? Ask',
    'See above for our question! \nCheck back in a few hours for another! \n\n🤷It may be easy, it may be hard. \n⌨️Either way, give it a tweet \n🔎Don\'t know it? Look it up \n❓Still unsure? Ask',
    '👆Check above for a fun code question! \nCheck back soon for another! \n\n🤷Maybe it\'s simple, maybe not \n🖱️Go ahead & tweet \n🧭Not sure? Search the web \n🗨️Still don\'t know? Ask',
    '👆Look up there for a fun code question! \nCome back shortly for another! \n\n🤷Maybe it\'s simple, maybe it\'s not \n📢Tell us in a tweet \n🧭Not sure? Search the web \n🗺️Still don\'t know? Ask',
    '🙈Do NOT look at the question above!👆 \n🚫Definitely don\'t answer it! \n\n🙉Fine, don\'t listen to me. \n🤖I\'m just a bot. \n📢Whatever, I know you\'re gonna do it anyway.',
    '🚨Alert! Alert!🚨 \n🙈Do NOT look at the question above!👆 \n🚫Definitely do NOT answer it! ',
    '💥Wild Code Question appeared! \n❓Fight or Run? \n\n You use Answer the Question \nIt was very effective!',
    'You\'ve found a code question! \n👆Look at the above tweet! \n\n⌨️While you\'re here, you may as well answer it.',
)


def get_reply():
    reply_to_tweet = choice(REPLIES)

    return reply_to_tweet
