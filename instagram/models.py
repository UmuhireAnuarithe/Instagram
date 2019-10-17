# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profile(models.Model):
    # photo = 
    biography = models.CharField(max_length =30)

    def __str__(self):
        return self.biography

class Image(models.Model):
    # image = 
    title = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    likes = models.IntegerField(default='none')
    comments = models.CharField(max_length =30)

    def __str__(self):
        return self.title
