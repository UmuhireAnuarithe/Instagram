# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField(upload_to = 'photos/',null=True)
    biography = models.CharField(max_length =30)

    def __str__(self):
        return self.biography

    @classmethod
    def search_user(cls,search_term):
        profiles = cls.objects.filter(biography__icontains=search_term)
        return profiles

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    title = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    likes = models.IntegerField(default='none')
    comments = models.CharField(max_length =30)

    def __str__(self):
        return self.title
