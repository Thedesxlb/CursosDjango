# Generated by Django 4.0.5 on 2022-07-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_rename_nombre_administrador_numero'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrador',
            options={'ordering': ['-created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='administrador',
            old_name='nivel',
            new_name='cuatrimestre',
        ),
    ]
