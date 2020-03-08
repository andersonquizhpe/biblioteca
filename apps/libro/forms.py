from django import forms 
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple

#Importamos los modelos, por ahora solo Libro
from apps.modelo.models import Libro

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo","fechaPublicacion","numeroPaginas","nombre_editorial","autor","resumen","imagen","genero","isbn"]

    
        widgets = {
            'fechaPublicacion': TextInput(attrs={'placeholder': 'AAAA-MM-DD'}),
            'isbn': TextInput(attrs={'placeholder':'9783161484100'}),
            'resumen': Textarea(attrs={'cols':80, 'rows':20, 'placeholder':'Resumen del libro'}),
        }

class FormularioModificarLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["numeroPaginas","autor","nombre_editorial","resumen","imagen","genero",]
        
        widgets = {
            'resumen': Textarea(attrs={'cols':80, 'rows':20, 'placeholder':'Resumen del libro'}),
        }