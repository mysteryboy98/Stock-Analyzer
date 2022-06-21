from email.mime import base
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import *

# Create your views here.

def SigninSignout(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'SigninSignout.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "SigninSignout.html", {
                "message" : "Invalid username and/or password"
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "SigninSignout.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensuring password matches confirmation
        password = request.POST["password"]
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            return render(request, "SigninSignout.html", {
                "message1": "Username or Email already Used."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "SigninSignout.html")

def home_view(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return HttpResponseRedirect(reverse("SigninSignout"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("SigninSignout"))

def tables_view(request):
    if request.user.is_authenticated:
        return render(request, "tables.html")
    else:
        return HttpResponseRedirect(reverse("SigninSignout"))

def bookmark_view(request):
    if request.user.is_authenticated:
        return render(request, "bookmark.html")
    else:
        return HttpResponseRedirect(reverse("SigninSignout"))