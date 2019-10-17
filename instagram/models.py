# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'photos/',null=True)
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
    caption = HTMLField()
    likes = models.IntegerField(default='none')
    comments = models.CharField(max_length =30)
    profile_photo = models.ForeignKey(Profile,null=True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title
