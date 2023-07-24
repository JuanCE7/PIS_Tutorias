from django.contrib import admin
from django.urls import path
from Academica.views import *  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name='login'),  
    path('inicio', inicio, name='inicio'),
    path('', inicio, name='inicio'),
    path('gestion_usuario', gestion_usuario, name='gestion_usuario'),
]
