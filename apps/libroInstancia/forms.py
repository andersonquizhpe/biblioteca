from django import forms
from django.forms import ModelForm, TextInput
# Importamos los modelos, por ahora solo Libro
from apps.modelo.models import LibroInstancia


class FormularioLibroInstacia(forms.ModelForm):
    class Meta:
        model = LibroInstancia
        fields = ['libro', 'estado', 'prestatario',
                  'fecha_devolucion']


class FormularioModificarLibro(forms.ModelForm):
    class Meta:
        model = LibroInstancia
        fields = ['libro', 'estado', 'prestatario',
                  'fecha_devolucion']
        widgets = {
            'libroinstancia_id': TextInput(attrs={'type': 'hidden'}),
        }
