"""projeto_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from projeto_web.paginas import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('casal_home', TemplateView.as_view(template_name="index.html")),
    #url(r'^$',TemplateView.as_view(template_name="index.html")),# pagina principal
    #path('LoginCasal',TemplateView.as_view(template_name="loginCasal.html")),
    #path('galeria', TemplateView.as_view(template_name="galeria.html")),#criar
    #path('inicio', LoginCasal.as_view(), name='logincasal'),
    path('', include('paginas.urls')),
    path('', include('cadastros.urls')),


]
