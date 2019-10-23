# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'photos/',null=True)
    biography = models.CharField(max_length =30)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.biography
    def save_profile(self):
        self.save()

    def update_profile(self):
        self.update()

    def delete(self):
        self.delete()
    
    @classmethod
    def search_user(cls,search_term):
        profiles = cls.objects.filter(username__username__icontains=search_term)
        return profiles

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    name = models.CharField(max_length =30)
    caption = HTMLField()
    comments = models.CharField(max_length =30)
    profile_photo = models.ForeignKey(Profile,null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def update_image(self):
        self.update()

    def delete(self):
        self.delete()


class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment = models.TextField()


    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()


    def delete(self):
        self.delete()
