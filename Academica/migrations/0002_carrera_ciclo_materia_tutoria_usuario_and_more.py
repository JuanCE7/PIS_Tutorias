# Generated by Django 4.2.3 on 2023-07-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('paralelo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitada', models.DateField()),
                ('fecha_planificada', models.DateField()),
                ('tema', models.CharField(max_length=100)),
                ('calificacion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retroalimentacion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Realizada', 'Realizada'), ('En Espera', 'En Espera')], default='Pendiente', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=30)),
                ('telefono', models.CharField(default='', max_length=30)),
                ('direccion', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=20)),
                ('rol', models.CharField(choices=[('Gestor', 'Gestor'), ('Tutor', 'Tutor'), ('Estudiante', 'Estudiante')], max_length=30)),
                ('tutorias', models.ManyToManyField(to='Academica.tutoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.usuario'),
        ),
        migrations.AddField(
            model_name='ciclo',
            name='materias',
            field=models.ManyToManyField(to='Academica.materia'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='ciclos',
            field=models.ManyToManyField(to='Academica.ciclo'),
        ),
    ]