from django.contrib import admin
from .models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'profesion', 'fecha_nacimiento']
    search_fields = ['rut', 'nombre', 'apellido', 'profesion']
    ordering = ['apellido', 'nombre']