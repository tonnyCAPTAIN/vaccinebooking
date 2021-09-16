"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from re import template
from django.contrib import admin
from django.urls import path, include


from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from book_appointment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),

   

    
    path('login/', 
    auth_views.LoginView.as_view(template_name ="registration/login.html"),
    name='login'),
    

    path('password_change/', 
    auth_views.PasswordChangeView.as_view(template_name ="registration/password_change_form.html"),
    name='password_change'),


    path('password_change_done/', 
    auth_views.PasswordChangeDoneView.as_view(template_name ="registration/password_change_done.html"),
    name='password_change_done'),

    # path('reset_password/', 
    # auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html'),
    # # subject_template_name='registration/password_reset_subject.txt',
    # # email_template_name='registration/password_reset_email.html',
    # # success_url='password_reset_done',

    # name='password_reset'),

    path('password_reset_done/',
    auth_views.PasswordResetDoneView.as_view(template_name ="registration/password_reset_done.html"), 
    name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name ="registration/password_reset_confirm.html"), 
    name='password_reset_confirm'),

    path('password_reset_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name ="registration/password_reset_complete.html"),
    name='password_reset_complete'),
    
    path('', include('book_appointment.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)