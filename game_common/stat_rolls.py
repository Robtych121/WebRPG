import random

def roll(dice, number):
    i = 0
    rolled = 0

    while i < dice:
        rolled += random.randint(1,dice)
        i += 1

    return rolled


def statRoll():
    first_roll = random.randint(1,6)
    second_roll = random.randint(1,6)
    third_roll = random.randint(1,6)
    fourth_roll = random.randint(1,6)

    array = [first_roll,second_roll,third_roll,fourth_roll]
    array.sort(reverse = True)
    array.pop()

    return sum(array)

def racialSTRModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 0
    if(race == 'Dwarf'):
        return 2
    if(race == 'Gnome'):
        return -1
    if(race == 'Half Orc'):
        return 0

def racialDEXModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Gnome'):
        return 2
    if(race == 'Half Orc'):
        return 0

def racialCONModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Orc'):
        return 1

def racialINTModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 2
    if(race == 'Dwarf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Orc'):
        return 0

def racialWISModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Orc'):
        return 0

def racialCHAModifier(race):
    if(race == 'Human'):
        return 1
    if(race == 'Elf'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Orc'):
        return 0