#from django.contrib import admin
#from django.urls import path ,include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('',include('app1.urls'))
#]

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('',include('app1.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    #path('', TemplateView.as_view(template_name='SigninSignout.html'), name='SigninSignout'),
]
