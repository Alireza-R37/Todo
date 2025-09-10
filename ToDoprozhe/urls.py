"""
URL configuration for ToDoprozhe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path , include
from tasks.views import home
from accounts.views import signup_view
from django.views.generic import TemplateView
from tasks.views import welcome  # ویوی جدید


urlpatterns = [
    path('', welcome, name='welcome'),                # صفحه خوش‌آمدگویی در روت
    #path('' ,home, name='home'),   
    path("admin/", admin.site.urls),
    path('tasks/', include("tasks.urls")),
    
    
]
