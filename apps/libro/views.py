from django.shortcuts import render, redirect
from apps.modelo.models import Genero, Libro, Lenguaje, Autor, LibroInstancia
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FormularioLibro, FormularioModificarLibro
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
# Create your views here.
"""Listar todos los libros"""
@login_required
def listarlibros(request):
    lista = Libro.objects.all()
    context ={
        'lista': lista
    }
    return render(request, 'libreria/listalibros.html', context)

"""Listar por id"""
@login_required
def detalle_libro(request, id):
	libro = Libro.objects.get(libro_id=id)
    
	context = {'object':libro}
	return render(request, 'libreria/librodetalle.html', context)

@login_required
def crearLibro(request):
	formulario = FormularioLibro(request.POST, request.FILES)
	#user
	usuario = request.user
	if usuario.groups.filter(name='administracion').exists() or usuario.groups.filter(name='bibliotecario').exists():
		if request.method == 'POST':
			print("libro en espras")
			formulario.is_valid(); print(formulario.errors) 
			if formulario.is_valid():
				datos = formulario.cleaned_data
				libro = Libro()
				libro.titulo = datos.get('titulo')
				libro.fechaPublicacion = datos.get('fechaPublicacion')
				libro.numeroPaginas = datos.get('numeroPaginas')
				libro.nombre_editorial = datos.get('nombre_editorial')
				libro.autor = datos.get('autor')
				libro.resumen = datos.get('resumen')
				libro.imagen = datos.get('imagen')
				libro.genero = datos.get('genero')
				libro.isbn = datos.get('isbn')
				print('todos los datos fueron guardados')
				libro.save()
				print("libro guardado")
				return redirect(listarlibros)
	else:
		return render(request, 'sin_acceso.html')
	
	context = {
		'formulario': formulario,
	}
	print('libro')
	return render(request, 'libreria/uc_libro.html', context)

@login_required
def actualizarLibro(request):
	libroid = request.GET['id']
	libro = Libro.objects.get(libro_id=libroid)
	usuario = request.user
	if usuario.groups.filter(name='administracion').exists() or usuario.groups.filter(name='bibliotecario').exists():
		if request.method == 'POST':
			formulario = FormularioModificarLibro(request.POST, request.FILES)
			if formulario.is_valid():
				print(formulario.errors)
				datos = formulario.cleaned_data
				libro.numeroPaginas = datos.get('numeroPaginas')
				libro.nombre_editorial = datos.get('nombre_editorial')
				libro.resumen = datos.get('resumen')
				libro.imagen = datos.get('imagen')
				libro.autor = datos.get('autor')
				libro.genero = datos.get('genero')
				print('todos los datos fueron guardados')
				print(formulario.errors)
				libro.save()
				print("libro guardado")
				print(formulario.errors)
				return redirect(listarlibros)
		else:
			formulario = FormularioModificarLibro(instance=libro)
			print(formulario.errors)
	else:
		return render(request, 'sin_acceso.html')
	
	context = {
		'formulario': formulario,
	}
	print('libro')
	return render(request, 'libreria/uc_libroE.html', context)

@login_required
def eliminarLibro(request, id):
	usuario = request.user
	if request.user.groups.filter(name="administracion").exists():
		libro = Libro.objects.get(libro_id=id)
		libro.delete()
		return redirect('/libros')
	else:
		return render(request, 'sin_acceso.html')
