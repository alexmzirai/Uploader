from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    location = forms.CharField(max_length=100)
    picture = forms.ImageField()

