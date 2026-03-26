from django.contrib import admin
from django.urls import path
from Line1 import views

urlpatterns = [
    path('', views.index, name='line1_home'),
    path('create/', views.create, name='line1_create'),
]