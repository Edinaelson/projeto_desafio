
#from django.views.generic.base import TemplateView
from django.views.generic import TemplateView

#from django.shortcuts import render

# Create your views here.

class LoginCasal(TemplateView):
    template_name = "loginCasal.html"

class LoginUsuario(TemplateView):
    template_name = "loginUsuario.html"
