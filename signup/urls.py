from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin_form),
    path('up/', views.signup_form)
]
