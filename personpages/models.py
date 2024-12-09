# In this file we created our Model, MissingPerson, and the necessary fields for the Missing Person

from django.db import models
from datetime import datetime

# Create your models here.
class MissingPerson (models.Model) :
    date_missing = models.DateField(default = datetime.today)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField(default=0)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=5)
    gender = models.CharField(max_length=5)
    race = models.CharField(max_length=5)
    class Meta:
        db_table = 'MissingTable'
def full_name(self):
    return '%s %s' % (self.first_name, self.last_name)
def __str__(self):
    return (self.first_name + " " + self.last_name)  
