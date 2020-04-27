from django.shortcuts import render
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('generatepassword/',views.password, name='password'),
     path('about-us/',views.about, name='about'),
]
