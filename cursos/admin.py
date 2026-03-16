from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'profesor', 'total_alumnos']
    search_fields = ['nombre', 'profesor__nombre', 'profesor__apellido']
    filter_horizontal = ['alumnos']  # Selector visual para la relación ManyToMany
    ordering = ['nombre']