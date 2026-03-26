from django.contrib import admin
from django.urls import path, include
from Line4 import views

urlpatterns = [
    path('', views.products, name='line4_products'),
    path('create/', views.create, name='line4_create'),
]