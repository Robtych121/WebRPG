import random

def statRoll():
    first_roll = random.randint(1,6)
    second_roll = random.randint(1,6)
    third_roll = random.randint(1,6)
    fourth_roll = random.randint(1,6)

    array = [first_roll,second_roll,third_roll,fourth_roll]
    array.sort(reverse = True)
    array.pop()

    return sum(array)

def classStatRole():
    stat1 = statRoll()
    stat2 = statRoll()
    stat3 = statRoll()
    stat4 = statRoll()
    stat5 = statRoll()
    stat6 = statRoll()

    array = [stat1,stat2,stat3,stat4,stat5,stat6]
    array.sort(reverse = True)

    return array

def racialSTRModifier(race):
    if(race == 'Dragonborn'):
        return 2
    if(race == 'Dwarf'):
        return 0
    if(race == 'Elf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Elf'):
        return 0
    if(race == 'Halfling'):
        return 0
    if(race == 'Half Orc'):
        return 2
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 0

def racialDEXModifier(race):
    if(race == 'Dragonborn'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Elf'):
        return 2
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Elf'):
        return 0
    if(race == 'Halfling'):
        return 2
    if(race == 'Half Orc'):
        return 0
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 0

def racialCONModifier(race):
    if(race == 'Dragonborn'):
        return 0
    if(race == 'Dwarf'):
        return 2
    if(race == 'Elf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Elf'):
        return 0
    if(race == 'Halfling'):
        return 0
    if(race == 'Half Orc'):
        return 1
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 0

def racialINTModifier(race):
    if(race == 'Dragonborn'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Elf'):
        return 0
    if(race == 'Gnome'):
        return 1
    if(race == 'Half Elf'):
        return 1
    if(race == 'Halfling'):
        return 0
    if(race == 'Half Orc'):
        return 0
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 1

def racialWISModifier(race):
    if(race == 'Dragonborn'):
        return 0
    if(race == 'Dwarf'):
        return 0
    if(race == 'Elf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Elf'):
        return 1
    if(race == 'Halfling'):
        return 0
    if(race == 'Half Orc'):
        return 0
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 0

def racialCHAModifier(race):
    if(race == 'Dragonborn'):
        return 1
    if(race == 'Dwarf'):
        return 0
    if(race == 'Elf'):
        return 0
    if(race == 'Gnome'):
        return 0
    if(race == 'Half Elf'):
        return 2
    if(race == 'Halfling'):
        return 0
    if(race == 'Half Orc'):
        return 0
    if(race == 'Human'):
        return 1
    if(race == 'Tiefling'):
        return 2