"""ResumeBuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from ResumeBuilder import views  
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('homepage1/', views.homepage1, name="homepage1"),
    path('login/', views.login, name="login"),
    path('sign-up/', views.sign, name="signup"),
    path('personal-details/', views.page1, name="page1"),
    path('educational-details/', views.page2, name="page2"),
    path('project-developed/', views.page3, name="page3"),
    path('experience-details/', views.page4, name="page4"),
    path('extra-details/', views.page5, name="page5"),
    path('resume/', views.resume, name="resume"),
    path('reset-password/', views.reset, name="reset"),
    path('logout/', views.logout, name="log"),
    path('download/', views.download, name="download"),
    path('resume2/', views.download1, name="download1"),
    path('selecttemp/', views.selecttemp, name="selecttemp"),
    path('warning/', views.warning, name="warning"),
]
