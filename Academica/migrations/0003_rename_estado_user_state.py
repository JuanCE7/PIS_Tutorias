# Generated by Django 4.2.3 on 2023-07-29 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0002_alter_user_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='estado',
            new_name='state',
        ),
    ]
