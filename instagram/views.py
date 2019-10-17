# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile,Image
# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request,'welcome.html',{'images':images})