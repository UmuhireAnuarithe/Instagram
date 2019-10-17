# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile,Image
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    return render(request,'welcome.html',{'images':images})


def search_user(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

        