from django.db import models
from datetime import datetime


# Create your models here.
class Messages(models.Model):
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    message = models.CharField(max_length=254, default='')
    character = models.CharField(max_length=254, default='')
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.date, self.character, self.message)