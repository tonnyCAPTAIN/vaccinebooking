
from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
# from django.contrib.auth import views as auth_views


app_name = 'book_appointment'

urlpatterns = [

    
    path('', views.homepage, name='home'),
    path('profile/', views.profile, name='profile'),
    path('venue/', views.venue, name='venue'),
    path('logout', views.logout, name='logout'),
    path('book/', views.book, name ='book'),
    path('book_second/', views.book_second, name ='book_second'),
    path('about/', views.about, name ='about'),
    path("login/", views.login, name="login"),
    path('doctor/', views.doctor, name='doctor'),

    
    
]