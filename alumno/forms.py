from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y'],
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = Alumno
        fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento']
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': 'Ej: 12.345.678-9'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del alumno'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido del alumno'}),
        }