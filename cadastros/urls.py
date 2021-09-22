from django.urls import path

from .views import CampoCreate

from .views import CampoUpdate

urlpatterns = [
    path('cadastros',CampoCreate.as_view(), name="cadastrar"),
] 