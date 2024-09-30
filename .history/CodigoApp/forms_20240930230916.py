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
        


class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = models.blog_details
        fields = ['blogerName', 'age','gender','mobileNo','email','desc','image'] 

    def __init__(self, *args, **kwargs):
        super(BlogDetailForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

class BlogCommentsDetailForm(forms.ModelForm):
    class Meta:
        model = models.commentMessage_detail
        fields = ['name','commentMsg', 'email','image'] 

    def __init__(self, *args, **kwargs):
        super(BlogDetailForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })            