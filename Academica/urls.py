from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),  
    path('inicio', inicio, name='inicio'),
    path('', inicio, name='inicio'),
    path('gestion_usuario', gestion_usuario, name='gestion_usuario'),
    path('administracion', administracion, name='gestion_usuario'),
]