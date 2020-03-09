from django.shortcuts import render, redirect
from apps.modelo.models import Genero, Libro, Lenguaje, Autor, LibroInstancia
from .forms import FormularioLibroInstacia
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def crearLibroInstancia(request):
    print("jjj")
    formulario = FormularioLibroInstacia(request.POST)
    if request.method == 'POST':
        print("dd")
        if formulario.is_valid():
            datos=formulario.cleaned_data
            libro = LibroInstancia()
            libro.fecha_devolucion = datos.get("fecha_devolucion")
            libro.estado = datos.get("estado")
            libro.libro = datos.get("libro")
            libro.prestatario = datos.get("prestatario")
            libro.save()
            return render(request, "libroInstancia/libro.html")
    
    context = {
        "formulario": formulario,
    }
    return render(request, "libroInstancia/uc_libro.html", context)
