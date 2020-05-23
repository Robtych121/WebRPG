from django.db import models
from datetime import datetime

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=254, default='', unique=True)
    user_id = models.IntegerField(default='')
    RACECHOICES = (
        ('Warrior', 'Warrior'),
        ('Bard', 'Bard'),
        ('Priest', 'Priest'),
        ('Druid', 'Druid'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Rogue', 'Rogue'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard')
    )
    role = models.CharField(max_length=254, default='', choices=RACECHOICES)
    RACECHOICES = (
        ('Human', 'Human'),
        ('Elf', 'Elf'),
        ('Dwarf', 'Dwarf'),
        ('Gnome', 'Gnome'),
        ('Half Orc', 'Half Orc')
    )
    race = models.CharField(max_length=254, default='', choices=RACECHOICES)
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    ) 
    main_character = models.CharField(max_length=254, default='No',choices=YESNOCHOICES)
    appearance = models.CharField(max_length=254, default='', blank=True)
    GENDERCHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ) 
    gender = models.CharField(max_length=254, default='', choices=GENDERCHOICES)
    gold = models.CharField(max_length=254, default='0')
    xp = models.CharField(max_length=254, default='0')
    level = models.CharField(max_length=254, default='1')
    strength = models.CharField(max_length=254, default='0')
    dexterity = models.CharField(max_length=254, default='0')
    constitution = models.CharField(max_length=254, default='0')
    intelligence = models.CharField(max_length=254, default='0')
    wisdom = models.CharField(max_length=254, default='0')
    charisma = models.CharField(max_length=254, default='0')
    created_date = models.DateField(default=datetime.now)
    banned = models.CharField(max_length=254, default='No',choices=YESNOCHOICES)

    def __str__(self):
        return self.name