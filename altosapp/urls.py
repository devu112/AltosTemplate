from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aha', views.aha, name='aha'),
    # path('adminlog', views.adminlog, name='adminlog'),
    # path('adminhome', views.adminhome, name='adminhome'),
]