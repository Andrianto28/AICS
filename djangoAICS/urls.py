"""
URL configuration for djangoAICS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from inputtingAutomation1 import views as iaview
from locationMovement3 import views as lmview

urlpatterns = [
    #1 - inputting Automation
    path('', include('inputtingAutomation1.urls')),
    #2 - Document Verification

    #3 - Location Movement
    path('', include('locationMovement3.urls')),
    path('admin/', admin.site.urls)
]
