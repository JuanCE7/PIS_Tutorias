from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Tutoring(models.Model):
    date_requested = models.DateField(blank=False)
    planned_date = models.DateField(blank=False)
    theme = models.CharField(max_length=100, blank=False)
    qualification = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=30, choices=(
        ('Pendiente', 'Pendiente'),
        ('Realizada', 'Realizada'),
        ('En Espera', 'En Espera'),
    ), default='Pendiente')

    def __str__(self):
        return "%s %s" % (self.theme, self.date_requested)
    
class User(models.Model):
    dni = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False, default='')
    email = models.EmailField(max_length=30, blank=False, default='')
    password = models.CharField(max_length=20, blank=False)
    rol = models.CharField(max_length=30, choices=(
        ('Gestor', ("Gestor")), ('Tutor', ("Tutor")),  ('Estudiante', ("Estudiante"))), default='Estudiante')
    tutorings = models.ManyToManyField(Tutoring,blank=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)

class Subject(models.Model):
    name = models.CharField(max_length=50, blank=False)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s impartida por %s" % (self.name, self.tutor)

class Cycle(models.Model):
    number = models.CharField(max_length=10, blank=False)
    parallel = models.CharField(max_length=10, blank=False)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return "%s %s" % (self.number, self.parallel)

class Career(models.Model):
    name = models.CharField(max_length=50, blank=False)
    cycles = models.ManyToManyField(Cycle)

    def __str__(self):
        return "%s" % self.name