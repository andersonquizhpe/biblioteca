from django import forms 
from django.forms import ModelForm

#Importamos los modelos, por ahora solo Libro
from apps.modelo.models import Libro

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','fechaPublicacion','numeroPaginas','nombre_editorial','autor','resumen','imagen','genero','isbn']