from django import forms
from django.forms import ModelForm
# Importamos los modelos, por ahora solo Libro
from apps.modelo.models import LibroInstancia


class FormularioLibroInstacia(forms.ModelForm):
    class Meta:
        model = LibroInstancia
        fields = ['libro', 'estado', 'prestatario',
                  'fecha_devolucion',]
        fieldsets = (
            (None, {
                'fields': ('libro', 'libroinstancia_id')
            }),
            ('Availability', {
                'fields': ('estado', 'fecha_devolucion', 'prestatario')
            }),
        )


class FormularioModificarLibro(forms.ModelForm):
    class Meta:
        model = LibroInstancia
        fields = ['libro', 'estado', 'prestatario',
                  'fecha_devolucion', 'libroinstancia_id']
