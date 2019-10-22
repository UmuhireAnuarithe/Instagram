from django import forms
from .models import Image,Profile,Comment

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile_photo','comments','username']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        exclude = ['username']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image','commenter']
        