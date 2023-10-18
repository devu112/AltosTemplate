from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('aha', views.aha, name='aha'),
    path('home', views.home, name='home'),

   
    path('adminlog', views.adminlog, name='adminlog'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('update_theme', views.update_theme, name='update_theme'),
]