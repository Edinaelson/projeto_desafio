#from django.conf import urls
from django.urls import path

from .views import LoginCasal
from .views import LoginUsuario

urlpatterns = [
    path('Não pega', LoginCasal.as_view(), name='logincasal'),        #1-login casal
    path('login', LoginUsuario.as_view(), name='loginusuario'),     #2-login usuario
] 