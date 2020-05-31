from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from templates_prac_app import  views

urlpatterns = [
    url(r'^$',views.help, name='help'),
    path('admin/', admin.site.urls),
]