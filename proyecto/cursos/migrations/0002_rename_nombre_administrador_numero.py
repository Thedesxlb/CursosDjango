# Generated by Django 4.0.5 on 2022-07-10 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='nombre',
            new_name='numero',
        ),
    ]
