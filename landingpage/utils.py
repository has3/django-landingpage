from django.conf import settings
import random
import math

def setting(name, default=None):
    """Return setting value for given name or default values"""
    return getattr(settings, name, default)

# multi-armed bandit stuff
# epsilon-first strategy

def pull_lever(lever):
    return

def choose():
    levers = [0,1,2]
    if random.random() < 0.1:
        # exploration!
        pull_lever(levers[random.randint(0,len(lever))])
    else:
        # exploration!
        for lever in levers:
            # calculate expectations of reward
            # this is trials of lever over given reward by that lever
            continue
        # choose the lever with the greatest expectation of reward
    # increment the number of times the chosen lever played
    # store result in redis

