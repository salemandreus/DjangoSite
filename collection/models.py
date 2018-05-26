from __future__ import unicode_literals

from django.db import models

class Day(models.Model):
    date = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    hightemp = models.CharField(max_length=255) 
    lowtemp = models.CharField(max_length=255)
    wind = models.CharField(max_length=255)
    rain = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
