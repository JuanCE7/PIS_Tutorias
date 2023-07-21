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