from django import forms
from django.contrib.auth.models import User
from . import models
import os
from django.conf import settings
from django.conf.urls.static import static    
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class BlogUserForm(forms.ModelForm):
    class Meta:
        model=models.UserDetails
        fields=['mobile','status','profile_pic']