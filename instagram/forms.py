from django import forms
from .models import Image ,Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile_photo','comments']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        exclude = ['username']
        