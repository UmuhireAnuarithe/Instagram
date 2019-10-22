# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Image ,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,NewProfileForm ,CommentForm

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
def new_profile(request):
  current_user = request.user
  new_profile = Profile.objects.filter(id=current_user.id)
  if request.method == 'POST':
      form = NewProfileForm(request.POST, request.FILES)
      if form.is_valid():
          picture = form.save(commit=False)
          picture.username = current_user
          picture.save()
      return redirect('profile')
  else:
      form = NewProfileForm()
  return render(request, 'new-profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def profile(request):
 current_user = request.user
 mypicture = Profile.objects.filter(username = current_user).first()
 return render(request, 'profile.html', { "mypicture":mypicture})


@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    comments = Comment.objects.all()
    if request.method == 'POST':
       form = CommentForm(request.POST)
       if form.is_valid():
           post_id = int(request.POST.get("idpost"))
           post = Post.objects.get(id = post_id)
           comment = form.save(commit=False)
           comment.username = request.user
           comment.post = post
           comment.save()
       return redirect('welcome')
    else:
            form = CommentForm()
    return render(request, 'comment.html', {"form": form ,'comments':comments})