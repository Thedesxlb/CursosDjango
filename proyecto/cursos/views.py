from django.shortcuts import render

from cursos.forms import CursosForm
from .models import Administrador
from django.shortcuts import get_object_or_404
# Create your views here.


def cursos(request):
    cursos = Administrador.objects.all()
    #.all() recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "cursos/cursos.html", {'cursos':cursos})

def confirmarEliminar(request, numero,
    confirmacion='cursos/eliminarCursos.html'):
    curso = get_object_or_404(Administrador, numero=numero)
    if request.method=='POST':
        curso.delete()
        cursos=Administrador.objects.all()
        return render(request,"cursos/cursos.html",
                {'cursos':cursos})
    return render(request, confirmacion, {'object':curso})


def confirmarEditar1(request, numero):
    curso = Administrador.objects.get(numero=numero)
    return render(request,"cursos/editarCurso.html",{'curso':curso})

def confirmarEditar2(request,numero):
    curso = get_object_or_404(Administrador, numero=numero)
    form= CursosForm (request.POST, instance=curso)
    if form.is_valid():
        form.save()
        curso=Administrador.objects.all()
        return render(request,"cursos/cursos.html",{'cursos':cursos})
    return render(request,"cursos/editarCurso.html",{'curso':curso})
    



def contacto(request):
    return render(request,"cursos/contacto.html")

