from django.contrib import admin

from .models import Administrador
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('numero','materia', 'profesor', 'cuatrimestre')
    search_fields = ('numero','materia', 'profesor', 'cuatrimestre')
    date_hierarchy ='created'
    list_filter = ('profesor', 'cuatrimestre')
    list_display_links=('numero','materia')
    list_editable=('profesor',)
    list_per_page=2

admin.site.register(Administrador, AdministrarModelo)


