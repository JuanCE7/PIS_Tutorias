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

def registro_usuario(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    cedula = request.POST['txtCedula']
    email = request.POST['txtEmail']
    password = request.POST['txtPassword']

    Usuario = Usuario.objects.create(
        nombre=nombre, apellido=apellido, cedula=cedula,email=email,password=password)
    return redirect('/')

def administracion(request):
    return render(request, "administracion.html")