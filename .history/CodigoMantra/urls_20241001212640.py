from django.contrib import admin
from django.urls import path
from CodigoApp import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='index'),
    
    # Patient register and login
    
    path('login', LoginView.as_view(template_name='CodigoApp/login.html')),
    path('signup', views.user_signup_view, name='signup'),
    path('dashboard', views.bloger_dashboard_view, name = 'dashboard'),
    path('addblog', views.add_blog_page, name = 'addblog'),
    path('update-blog/<slug>', views.update_blog, name='update-blog'),
    path('delete-blog/<int:pk>', views.delete_blog, name='delete-blog'),
    path('view-all-blogs', views.view_all_blogs_page, name='view-all-blogs'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle-like'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)