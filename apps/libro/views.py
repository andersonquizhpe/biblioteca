from django.shortcuts import render
from apps.modelo.models import Genero, Libro, Lenguaje, Autor, LibroInstancia
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.libro.forms import FormularioLibro
from django.views import generic

from django.urls import reverse_lazy
# Create your views here.
"""Listar todos los libros"""
def listarlibros(request):
    lista = Libro.objects.all()
    context ={
        'lista': lista
    }
    return render(request, 'libreria/listalibros.html', context)

"""Listar por id"""
def detalle_libro(request, id):
	libro = Libro.objects.get(libro_id=id)
    
	context = {'object':libro}
	return render(request, 'libreria/librodetalle.html', context)


class LibroCreateView(generic.CreateView):
	model = Libro
	#Caracteristicas especiales para el form de crear
	form_class = FormularioLibro
	template_name = 'libreria/uc_libro.html'

class LibroUpdateView(generic.UpdateView):
	model = Libro
	form_class = FormularioLibro
	template_name = 'libreria/uc_libro.html'	


class LibroDeleteView(generic.DeleteView):
	model = Libro
	success_url = reverse_lazy('libros')