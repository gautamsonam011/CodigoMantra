from django import forms
from django.contrib.auth.models import User
from . import models
import os
from django.conf import settings
from django.conf.urls.static import static

   
class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.doctor_details
        # status = True
        fields = ['name','age','gender','degree', 'mobile', 'weekday', 'hospitalName', 'address','email','time_in', 'time_out','experience','specialization','no_of_patient','brief','image', 'status'] 
  
    
        
        
        
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['mobile','status','symptoms','profile_pic']