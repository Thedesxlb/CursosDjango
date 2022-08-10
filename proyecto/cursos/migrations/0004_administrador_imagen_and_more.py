# Generated by Django 4.0.5 on 2022-07-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_administrador_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='cuatrimestre',
            field=models.TextField(verbose_name='Num_Cuatri'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='materia',
            field=models.TextField(verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='numero',
            field=models.CharField(max_length=12, verbose_name='Num_Curso'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='profesor',
            field=models.TextField(verbose_name='Profesor(a)'),
        ),
    ]