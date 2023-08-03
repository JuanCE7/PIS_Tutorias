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

    def _str_(self):
        return "%s %s" % (self.theme, self.date_requested)
    
class Subject(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def _str_(self):
        return "%s impartida por %s" % (self.name, self.tutor)

class Cycle(models.Model):
    number = models.CharField(max_length=10, blank=False)
    parallel = models.CharField(max_length=10, blank=False)
    subjects = models.ManyToManyField(Subject)

    def _str_(self):
        return "%s %s" % (self.number, self.parallel)

class Career(models.Model):
    name = models.CharField(max_length=50, blank=False)
    cycles = models.ManyToManyField(Cycle)

    def _str_(self):
        return "%s" % self.name
    
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
    subjects = models.ManyToManyField(Subject, blank = True)
    cycles = models.ManyToManyField(Cycle, blank = True)
    careers = models.ManyToManyField(Career, blank = True)

    def _str_(self):
        return "%s %s" % (self.name,self.last_name)