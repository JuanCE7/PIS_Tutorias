<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from Academica.views import *  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name='login'),  
    path('inicio', inicio, name='inicio'),
    path('', inicio, name='inicio'),
    path('gestion_usuario', gestion_usuario, name='gestion_usuario'),
=======
# urls.py (del proyecto)

from django.contrib import admin
from django.urls import path
from Academica.views import login  # Importa tu vista de login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),  # Asigna un nombre a la URL para poder referenciarla en las plantillas
    # Agrega otras URLs de tu proyecto si es necesario
>>>>>>> e7950d7a5ecd7e31a3764b3355a8f69c7e16408c
]
