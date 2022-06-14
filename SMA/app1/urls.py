from turtle import home
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from app1 import views

urlpatterns = [
    path('', views.SigninSignout, name='SigninSignout'),
]
