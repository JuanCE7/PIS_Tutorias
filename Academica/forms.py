from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'email', 'telefono', 'direccion','password', 'rol']

class TutoriaForm(forms.ModelForm):
    class Meta:
        model = Tutoria
        fields = ['tema', 'fecha_solicitada', 'fecha_planificada', 'estado']

class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = ['numero', 'paralelo']

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'docente']