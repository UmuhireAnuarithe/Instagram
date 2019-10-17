# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    likes = models.IntegerField(default='none')
    comments = models.CharField(max_length =30)