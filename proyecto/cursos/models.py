from django.db import models


# Create your models here.

class Administrador(models.Model): #Define la estructura de nuestra tabla
    numero = models.CharField(max_length=12, verbose_name="Num_Curso") #Texto corto
    materia = models.TextField(verbose_name="Curso") #Texto largo
    profesor = models.TextField(verbose_name="Profesor(a)")
    cuatrimestre = models.TextField(verbose_name="Carrera")
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]

    def __str__(self):
        return self.materia
    #     #Indica que se mostrará el nombre como valor en la tabla


