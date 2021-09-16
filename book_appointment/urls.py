
from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
# from django.contrib.auth import views as auth_views


app_name = 'book_appointment'

urlpatterns = [

    
    path('', views.homepage, name='home'),
    path('profile/', views.profile, name='profile'),
    #path('accounts/register/', views.register, name='register'),
    
    path('logout', views.logout, name='logout'),
    path('book/', views.book, name ='book'),
    path('about/', views.about, name ='about'),
    path("login/", views.login, name="login"),
    path('doctor/', views.doctor, name='doctor'),

    

    
    
]