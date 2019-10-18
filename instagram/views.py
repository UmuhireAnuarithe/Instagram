# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Image
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm

@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    profiles= Profile.objects.all()
    return render(request,'welcome.html',{'profiles':profiles,'images':images})


def search_user(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new.html', {"form": form})  



@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    user_edit = Profile.objects.get(username__id=current_user.id)
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            print('success')
          
        form=ProfileForm(instance=request.user.profile)
        print('error')


    return render(request,'edit_profile.html',locals())  