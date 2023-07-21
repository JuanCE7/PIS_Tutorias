from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre +self.apellido

class Tutoria(models.Model):
    fecha = models.DateField()
    tema = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retroalimentacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tema + self.fecha