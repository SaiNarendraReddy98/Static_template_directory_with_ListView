from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class School_list(ListView):
    model = School
    context_object_name = 'nari'
    #ordering = ['sname']
    #queryset = School.objects.filter(pk=1)

class School_detail(DetailView):
    model = School
    context_object_name = 'sclobj'


class School_Create(CreateView):
    model = School
    fields = '__all__'


class School_Update(UpdateView):
    model = School
    fields = '__all__'


class School_Delete(DeleteView):
    model = School
    context_object_name = 'schoolobj'
    success_url = reverse_lazy('School_list')
    

class Student_Create(CreateView):
    modal = Student
    fields = '__all__'



    




    
    