"""
URL configuration for subwayproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Line1 import views as line1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', line1_views.index, name='home'),
    path('line1/', include('Line1.urls')),
    path('line2/', include('Line2.urls')),
    path('line4/', include('Line4.urls')),
    path('line6/', include('Line6.urls')),
]
