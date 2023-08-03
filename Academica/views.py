from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import *
from django.views.decorators.csrf import csrf_protect

user1 = User.objects

@csrf_protect
def login_view(request):
    flogin = LoginForm(request.POST or None)
    if request.method == 'POST':
        if flogin.is_valid():
            datos = flogin.cleaned_data
            email = datos.get("email")
            passw = datos.get("password")
            numEncontrados = User.objects.filter(email = email, password=passw).count()
            user = User.objects.filter(email=email, password=passw).first()
            
            print(numEncontrados)
            if numEncontrados > 0:
                print(user.email)
                user.state = True  # Asigna el estado "True" al usuario autenticado
                user1.state = True
                user1.rol = user.rol
                user.save() # Guarda el dcambio en la base de datos
                messages.success(request, 'Bienvenido')
                return render(request,'index.html', {'user':user})  # Redirige a la página de inicio
            else:
                messages.warning(request, 'Credenciales Incorrectas')
                return redirect('login')
    context = {
        'form': flogin,
    }
    return render(request, "login.html", context)

def index(request):
    return render(request, "index.html", {'user': user1}) 

def admins(request):
    return render(request, "base_admin.html", {'user': user1}) 

def subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject')
    else:
        form = SubjectForm()
    subjects = Subject.objects.all()
    return render(request, "subject_list.html", {'user': user1, 'subjects': subjects, 'form':form})

def logout(request):
    user1.state = False
    return render(request, "index.html", {'user': user1})

@csrf_protect
def register(request):
    f = UserForm(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = User()
            c.rol= 'Estudiante'
            c.name = datos.get("name")
            c.last_name = datos.get("last_name")
            c.dni = datos.get("dni")
            c.email = datos.get("email")
            c.password = datos.get("password")
            if c.save() != True:
                messages.warning(request, 'Registrado Correctamente')
                return redirect(login_view)
    context = {
        'form': f,
    }
    return render(request, "register.html", context)


def materia_update(request, pk):
    materia = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('subject')
    else:
        form = SubjectForm(instance=materia)
    return render(request, 'subject_list.html', {'form': form})

def materia_delete(request, pk):
    materia = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        materia.delete()
        return redirect('subject')
    return render(request, 'materia_confirm_delete.html', {'materia': materia})