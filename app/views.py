from django.shortcuts import render
from app.models import *
from django.views.generic import ListView

# Create your views here.

class School_list(ListView):
    model = School
    context_object_name = 'nari'
    #ordering = ['sname']
    #queryset = School.objects.filter(pk=1)

