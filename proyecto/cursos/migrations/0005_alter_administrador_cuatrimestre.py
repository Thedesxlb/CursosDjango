# Generated by Django 4.0.5 on 2022-07-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_administrador_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='cuatrimestre',
            field=models.TextField(verbose_name='Carrera'),
        ),
    ]
