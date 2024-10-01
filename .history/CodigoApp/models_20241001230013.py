from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from CodigoApp.uitls import *
from datetime import datetime
from django.utils import timezone
ext_validator = FileExtensionValidator(['png','jpg','pdf','PNG'])

def validate_file_mimetype(file):
    accept = ['image/png', 'image/jpeg','application/pdf', 'image/PNG','image/JPG']

class UserDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/')
    mobile = models.CharField(max_length=20,null=False, default='')
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_id(self):
        return self.user.id
    
from datetime import time 

def default_time():
    return time(hours=12,minute=30) 

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

WEEK_CHOICES = (
        ('Weekdays','Weekdays'),
        ('Weekend','Weekend'),
    )

class blog_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    blogerName = models.CharField(max_length=50, null=False, blank=False)
    degree = models.CharField(max_length=500, null=False, blank=False)
    mobileNo = models.CharField(max_length=20,null=False, default='')
    address = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(upload_to='uploads/')
    age = models.IntegerField(null=True)
    experience = models.IntegerField(default=False)
    gender = models.CharField(max_length=500, null=True, choices=GENDER_CHOICES)
    brief = models.TextField(max_length=200, null=True)
    heading = models.CharField(max_length=200, null=True)
    email = models.EmailField(blank=True)
    created_date = models.DateTimeField(auto_now=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True)

    def _str_(self):
        return self.name
    
    @property
    def get_id(self):
        return self.user.id
    
    # def save(self,  *args, **kwargs):
        # self.slug = generate_doctor_slug(self.name)
        # super(doctor_details, self).save(*args, **kwargs)

class commentMessage_detail(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(blank=True)
    commentMsg = models.CharField(max_length=500,null=False,blank=False)
    image = models.ImageField(upload_to='uploads/')
    status=models.BooleanField(default=False)
    createdDate = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.disease+")"
    
    # def save(self,  *args, **kwargs):
    #     self.slug = generate_patient_slug(self.patientName)
    #     super(Patient_detail, self).save(*args, **kwargs)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)   
     
# class count_of_likes_blog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     likeCount = models.BooleanField(max_length=500,null=False,blank=False)
#     email = models.EmailField(default='')
#     desc = models.CharField(max_length=500,null=False,blank=False)
#     image = models.ImageField(upload_to='uploads/')
#     status=models.BooleanField(default=False)
#     createdDate = models.DateField(auto_now=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     class Meta:
#         unique_together = ('user', 'post')

