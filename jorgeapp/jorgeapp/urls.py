"""
URL configuration for jorgeapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from jorgeluisapp.views import  JuanAPIView , CristianAPIView, CamiloAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jorgeluisapp.urls')),
    path('cris/', CristianAPIView.as_view()),
    path('juan/', JuanAPIView.as_view()),
    path('camilo/', CamiloAPIView.as_view()),
    
     
    
]
