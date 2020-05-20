from django.db import models
from datetime import datetime

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=254, default='', unique=True)
    user_id = models.IntegerField(default='')
    role = models.CharField(max_length=254, default='')
    race = models.CharField(max_length=254, default='')
    appearance = models.CharField(max_length=254, default='')
    gender = models.CharField(max_length=254, default='')
    gold = models.CharField(max_length=254, default='')
    xp = models.CharField(max_length=254, default='')
    level = models.CharField(max_length=254, default='')
    strength = models.CharField(max_length=254, default='')
    dexterity = models.CharField(max_length=254, default='')
    constitution = models.CharField(max_length=254, default='')
    wisdom = models.CharField(max_length=254, default='')
    charisma = models.CharField(max_length=254, default='')
    created_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name