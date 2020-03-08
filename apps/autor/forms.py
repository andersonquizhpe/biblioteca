from django import forms 
from django.forms import ModelForm

#Importamos los modelos, por ahora solo Libro
from apps.modelo.models import Autor

class FormularioAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','email']

class FormularioModificarAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido','email']