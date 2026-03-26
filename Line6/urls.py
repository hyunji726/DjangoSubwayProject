from django.contrib import admin
from django.urls import path, include
from Line6 import views

urlpatterns = [
    path('', views.store, name='line6_store'),
    path('create/', views.create, name='line6_create'),
]