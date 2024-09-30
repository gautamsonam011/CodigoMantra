from django.shortcuts import render,redirect, get_object_or_404
from . import forms, models
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect,HttpResponseServerError
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import logout 
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone


# Home page 

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'CardigoApp/index.html')

# user registration page

def user_signup_view(request):
    userForm=forms.UserForm()
    blogForm=forms.BlogUserForm()
  
    mydict={'userForm':userForm,'blogForm':blogForm}
    if request.method=='POST':
        userForm=forms.userForm(request.POST)
        blogForm=forms.blogForm(request.POST,request.FILES)
        if userForm.is_valid() and blogForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            blogUser=blogForm.save(commit=False)
            blogUser.user=user
            blogUser=blogUser.save()
            my_bloger_group = Group.objects.get_or_create(name='Bloger')
            my_bloger_group[0].user_set.add(user)
        return HttpResponseRedirect('blogerlogin')
    return render(request,'CodigoApp/registration.html',context=mydict)


#-----------for checking user is auth bloger or not
def is_authUser(user):
    return user.groups.filter(name='Bloger').exists()
   

def afterlogin_view(request):   
    if is_authUser(request.user):
        accountapproval= models.UserDetails.objects.all().filter(user_id = request.user.id)
        if accountapproval:
            return redirect('dashboard')
        else:
            return render(request,'Codigo/bloger_wait_for_approval.html')   
    
    
def logout_request(request):
    if is_authUser(request.user):
        logout(request)
        return redirect("/login") 
    else:
        return JsonResponse({'error': 'Form is not valid.'}, status=400) 

    
        
@login_required(login_url='login')
@user_passes_test(is_authUser)
def bloger_dashboard_view(request):
    blog = models.blog_details.objects.get(user_id=request.user.id)
    mydict={
        'admitDate':blog.admitDate,
    }
    return render(request,'Appointment/patient-dashboard.html',context=mydict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    mydict={
        'profile_pic':patient.profile_pic,
    }
    return render(request,'Appointment/patient-dashboard.html',context=mydict)