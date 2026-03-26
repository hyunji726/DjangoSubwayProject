from django.contrib import admin
from django.urls import path
from Line2 import views

urlpatterns = [
    path('', views.about, name='line2_about'),
    path('create/', views.create, name='line2_create'),
]