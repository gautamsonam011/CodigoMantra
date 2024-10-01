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
    return render(request,'CodigoApp/index.html')

# user registration page

def user_signup_view(request):
    userForm=forms.UserForm()
    BlogerForm=forms.BlogerForm()
  
    mydict={'userForm':userForm,'BlogerForm':BlogerForm}
    if request.method=='POST':
        userForm=forms.UserForm(request.POST)
        BlogerForm=forms.BlogerForm(request.POST,request.FILES)
        if userForm.is_valid() and BlogerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=BlogerForm.save(commit=False)
            patient.user=user
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='BLOG')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'CodigoApp/registration.html',context=mydict)


#-----------for checking user is auth bloger or not
def is_authUser(user):
    return user.groups.filter(name='BLOG').exists()
   

def afterlogin_view(request):   
    if is_authUser(request.user):
        # accountapproval= models.UserDetails.objects.all().filter(user_id = request.user.id)
        # if accountapproval:
        return redirect('dashboard')
        # else:
        #     return render(request,'CodigoApp/bloger_wait_for_approval.html')   
    
    
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
    return render(request,'CodigoApp/dashboard.html',context=mydict)


@login_required(login_url='login')
@user_passes_test(is_authUser)
def blog_dashboard_view(request):
    blog = models.blog_details.objects.get(user_id=request.user.id)
    mydict={
        'profile_pic':blog.profile_pic,
    }
    return render(request,'CodigoApp/dashboard.html',context=mydict)



# ===========================Start Add Blog Details ==================

@login_required(login_url='login')
@user_passes_test(is_authUser)
def add_blog_page(request):
    if request.method == 'POST':
        form = forms.BlogDetailForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.status=True
            instance.save()
            return redirect('view-all-patient')
    else:
        form = forms.BlogDetailForm()
    return render(request, 'CodigoApp/addblogs.html', {'form':form})


@login_required(login_url='login')
@user_passes_test(is_authUser)
def update_blog(request,slug):
    fetchData = models.blog_details.objects.get(user_id=request.user.id, slug=slug)
  
    if request.method=='POST':
        form=forms.BlogDetailForm(request.POST,request.FILES,instance=fetchData)
        if form.is_valid():
            form.save()
            return redirect('/view-all-patient', fetchData.slug)
    else:
        form=forms.BlogDetailForm(instance=fetchData)
    return render(request,'CodigoApp/addblogs.html',{'form':form})
    


@login_required(login_url='login')
@user_passes_test(is_authUser)
def delete_blog(request,pk):
    fetchData = models.blog_details.objects.filter(user_id=request.user.id, id=pk)
    fetchData.delete()
    fetchData=models.blog_details.objects.all().filter(status=True,user_id=request.user.id)
    return render(request,'CodigoApp/viewblogs.html', {'fetchData':fetchData})

@login_required(login_url='login')
@user_passes_test(is_authUser)
def view_all_blogs_page(request):
    newData = models.blog_details.objects.all().filter(user_id=request.user.id)
    return render(request,'CodigoApp/viewblogs.html',{'newData':newData})


# ============== Comments =================

@login_required(login_url='login')
@user_passes_test(is_authUser)
def add_blog_comments_page(request):
    if request.method == 'POST':
        form = forms.BlogCommentsDetailForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user.id
            instance.status=True
            instance.save()
            return redirect('view-all-patient')
    else:
        form = forms.BlogCommentsDetailForm()
    return render(request, 'CodigoApp/addblogComments.html', {'form':form})


@login_required(login_url='login')
@user_passes_test(is_authUser)
def delete_blog_comment(request,pk):
    fetchData = models.commentMessage_detail.objects.filter(user_id=request.user.id, id=pk)
    fetchData.delete()
    fetchData=models.commentMessage_detail.objects.all().filter(status=True,user_id=request.user.id)
    return render(request,'CodigoApp/viewblogComments.html', {'fetchData':fetchData})

@login_required(login_url='login')
@user_passes_test(is_authUser)
def view_all_blogs_comments(request):
    newData = models.commentMessage_detail.objects.all().filter(user_id=request.user.id)
    return render(request,'CodigoApp/viewblogComments.html',{'newData':newData})

# ============ Like =================== 
    
def toggle_like(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)
    like, created = models.count_of_likes_blog.objects.get_or_create(user=request.user, post=post)

    if not created:
        # If the like already existed, remove it (unlike)
        like.delete()
    # Redirect back to the post or wherever you want
    return redirect('post_detail', post_id=post.id)    