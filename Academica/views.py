<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def login(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')

def gestion_usuario(request):
    usuariosListados = Usuario.objects.all()
    return render(request, 'gestion_usuario.html', {"usuarios":usuariosListados})
=======
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
>>>>>>> e7950d7a5ecd7e31a3764b3355a8f69c7e16408c
