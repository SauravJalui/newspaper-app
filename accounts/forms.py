from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''This code is to extend the existing UserCreationForm to add a new field'''
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)
    
class CustomUserChangeForm(UserChangeForm):
    '''This code is to extend the existing UserChangeForm'''
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields