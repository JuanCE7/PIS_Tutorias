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
                return redirect(register)
    context = {
        'form': f,
    }
    return render(request, "register.html", context)

def materia_update(request, subject_id):
    materia = get_object_or_404(Subject, pk=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materia_update', subject_id=subject_id)
    else:
        form = SubjectForm(instance=materia)
    return render(request, 'edit_materia.html', {'form': form, 'materia':materia})

def materia_delete(request, subject_id):
    materia = get_object_or_404(Subject, pk=subject_id)
    materia.delete()
    return redirect('subject')
    #return render(request, 'materia_confirm_delete.html', {'materia': materia})


def tutoring(request):
    tutores = User.objects.filter(rol='Tutor')
    return render(request, "tutoring.html", {'user': user1, 'tutores': tutores}) 


def tutorias_tutor(request, tutor_id):
    tutor = User.objects.get(pk=tutor_id)
    tutorias = Tutoring.objects.filter(user=tutor)
    return render(request, 'tutorias_tutor.html', {'user': user1,'tutor': tutor, 'tutorias': tutorias})


@csrf_protect
def cycles(request):
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cycles')
    else:
        form = CycleForm()
    cycles = Cycle.objects.all()
    return render(request, "cycles_list.html", {'user': user1, 'cycles': cycles, 'form':form})

@csrf_protect
def editar_cycle(request, ciclo_id):
    cycle = get_object_or_404(Cycle, pk=ciclo_id)
    if request.method == 'POST':
        form = CycleForm(request.POST, instance=cycle)
        if form.is_valid():
            form.save()
            print('metodoPost')
            # Redirigir a la página de detalle del ciclo editado con su ID
            return redirect('editar_cycle', ciclo_id=ciclo_id)
    else:
        form = CycleForm(instance=cycle)
    
    print('metodo get')
    return render(request, 'edit_cycle.html', {'form': form, 'cycle':cycle})

def eliminar_cycle(request, ciclo_id):
    cycle = get_object_or_404(Cycle, pk=ciclo_id)
    cycle.delete()
    print('estamos eliminando')
        #return redirect('cycles')
    return render(request, 'cycles_list.html', {'cycle': cycle})
