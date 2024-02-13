"""
URL configuration for project36 project.

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
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('School_list/',School_list.as_view(),name='School_list'),
    path('School_Create/',School_Create.as_view(),name='School_Create'),
    path('Student_Create/',Student_Create.as_view(),name='Student_Create'),


    re_path('^delete/(?P<pk>\d+)/',School_Delete.as_view(),name='School_Delete'),
    re_path('^update/(?P<pk>\d+)/',School_Update.as_view(),name='School_Update'),
    re_path('(?P<pk>\d+)/',School_detail.as_view(),name='scldetail'),
    #re_path('^update/(?P<pk>\d+)/',School_Update.as_view(),name='School_Update'),



]
