# Generated by Django 4.2.2 on 2023-07-01 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0002_rename_fecha_creacion_tareas_fecha_vencimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tareas',
            old_name='fecha_publicación',
            new_name='fecha_publicacion',
        ),
    ]
