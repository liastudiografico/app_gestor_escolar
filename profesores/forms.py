from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y'],
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = Profesor
        fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'profesion']
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'profesion': 'Profesión',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'placeholder': 'Ej: 12.345.678-9'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del profesor'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido del profesor'}),
            'profesion': forms.TextInput(attrs={'placeholder': 'Ej: Licenciado en Matemáticas'}),
        }