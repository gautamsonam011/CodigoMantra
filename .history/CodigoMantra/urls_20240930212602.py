from django.contrib import admin
from django.urls import path
from CodigoApp import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home_view,name='index'),
    
    # Patient register and login
    
    path('patientlogin', LoginView.as_view(template_name='Appointment/login.html')),
    path('patientsignup', views.patient_signup_view, name='patientsignup'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)