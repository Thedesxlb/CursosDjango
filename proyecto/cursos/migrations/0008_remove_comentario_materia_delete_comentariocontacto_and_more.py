# Generated by Django 4.0.5 on 2022-08-10 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_comentariocontacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='materia',
        ),
        migrations.DeleteModel(
            name='ComentarioContacto',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
