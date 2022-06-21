from turtle import home
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from app1 import views

urlpatterns = [
    path('', views.SigninSignout, name='SigninSignout'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup_view,name='signup'),
    path('home',views.home_view,name='home'),
    path('tables',views.tables_view,name='tables'),
    path('bookmark',views.bookmark_view,name='bookmark'),
    path('logout',views.logout_view,name='logout'),
    
]