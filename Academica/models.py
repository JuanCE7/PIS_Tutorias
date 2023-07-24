from django.db import models

class Tutoria(models.Model):
    fecha_solicitada = models.DateField(blank=False)
    fecha_planificada = models.DateField(blank=False)
    tema = models.CharField(max_length=100, blank=False)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retroalimentacion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=30, choices=(
        ('Pendiente', 'Pendiente'),
        ('Realizada', 'Realizada'),
        ('En Espera', 'En Espera'),
    ), default='Pendiente')

    def __str__(self):
        return "%s %s" % (self.tema, self.fecha_solicitada)

class Usuario(models.Model):
    cedula = models.CharField(max_length=10, blank=False)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False, default='')
    email = models.EmailField(max_length=30, blank=False, default='')
    telefono = models.CharField(max_length=30, blank=False, default='')
    direccion = models.CharField(max_length=70, blank=False)
    password = models.CharField(max_length=20, blank=False)
    rol = models.CharField(max_length=30, choices=(
        ('Gestor', 'Gestor'),
        ('Tutor', 'Tutor'),
        ('Estudiante', 'Estudiante'),
    ))
    tutorias = models.ManyToManyField(Tutoria)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class Materia(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    docente = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "%s impartida por %s" % (self.nombre, self.docente)

class Ciclo(models.Model):
    numero = models.CharField(max_length=10, blank=False)
    paralelo = models.CharField(max_length=10, blank=False)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return "%s %s" % (self.numero, self.paralelo)

class Carrera(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    ciclos = models.ManyToManyField(Ciclo)

    def __str__(self):
        return "%s" % self.nombre
