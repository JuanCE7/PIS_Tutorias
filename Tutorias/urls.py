# urls.py (del proyecto)

from django.contrib import admin
from django.urls import path
from Academica.views import login  # Importa tu vista de login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),  # Asigna un nombre a la URL para poder referenciarla en las plantillas
    # Agrega otras URLs de tu proyecto si es necesario
]
