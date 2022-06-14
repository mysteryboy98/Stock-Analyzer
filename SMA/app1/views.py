#from django.shortcuts import render

from django.shortcuts import render,HttpResponse

# Create your views here.

def SigninSignout(request):
    return render(request, 'SigninSignout.html')
    