# Generated by Django 4.2.3 on 2023-07-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
