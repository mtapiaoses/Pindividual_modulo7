# Generated by Django 4.2.2 on 2023-07-01 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='fecha_creacion',
            new_name='fecha_vencimiento',
        ),
    ]
