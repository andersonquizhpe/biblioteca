from django import forms 
from django.forms import ModelForm

#Importamos los modelos, por ahora solo Libro
from apps.modelo.models import Genero

class FormularioGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']

class FormularioModificarGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']