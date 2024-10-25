from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))
    phone = forms.CharField(required=False, max_length=15)
    is_available = forms.BooleanField(required=False) 

    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'is_available'] 
