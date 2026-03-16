from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'profesor', 'alumnos']
        labels = {
            'nombre': 'Nombre del Curso',
            'profesor': 'Profesor Asignado',
            'alumnos': 'Alumnos del Curso',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Matemáticas 1°A'}),
            'profesor': forms.Select(),
            'alumnos': forms.CheckboxSelectMultiple(),
        }