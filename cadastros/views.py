#from django.shortcuts import render

from django.forms.models import Field
from django.views.generic.edit import CreateView, UpdateView

from .models import Campo

from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo
    fields = ['email']
    template_name = 'cadastros/formLogin.html'
    success_url = reverse_lazy('admin')

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['email', 'senha']
    template_name = 'cadastros/formLogin.html'
    #success_url = reverse_lazy('')


