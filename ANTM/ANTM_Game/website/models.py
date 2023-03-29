from django.db import models
from datetime import datetime

class Contestants(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(default=20, null=True)
    hometown = models.CharField(max_length=100, default='', null=True)
    cycle = models.IntegerField(default=1, null=True)
    elim = models.CharField(max_length = 5, default='14th', null=True)
