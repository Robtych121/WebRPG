import random

def roll(dice, number):
    i = 0
    rolled = 0

    while i < dice:
        rolled += random.randint(1,dice)
        i += 1

    return rolled