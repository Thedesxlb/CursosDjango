from django import forms

from.models import Administrador


class CursosForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['materia','profesor','cuatrimestre', 'turno']