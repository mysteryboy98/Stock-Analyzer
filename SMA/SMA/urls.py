

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',include('app1.urls')),
    path('admin/', admin.site.urls),
]
