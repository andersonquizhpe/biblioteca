from django.shortcuts import render, redirect
from apps.modelo.models import Genero, Libro, Lenguaje, Autor, LibroInstancia
from .forms import FormularioLibroInstacia, FormularioModificarLibro
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


#listar libros prestados
@login_required
def listarPrestamos(request):
    #listar si es bibliotecario
    usuario = request.user
    if usuario.groups.filter(name='bibliotecario').exists():
        lista = LibroInstancia.objects.filter(estado='p')
        listade = LibroInstancia.objects.filter(estado='d')
        context ={
            'lista': lista,
            'listade': listade,
        }
        print("hola")
        return render(request, "libroInstancia/libro.html", context)
    else:
        return render(request, "sin_acceso.html")

@login_required
def crearLibroInstancia(request):
    print("jjj")
    #si es bibliotecario puede añadir prestamos
    usuario = request.user
    formulario = FormularioLibroInstacia(request.POST)
    if usuario.groups.filter(name='bibliotecario').exists():
        if request.method == 'POST':
            print("dd")
            if formulario.is_valid():
                datos=formulario.cleaned_data
                libro = LibroInstancia()
                libro.fecha_devolucion = datos.get("fecha_devolucion")
                libro.estado = datos.get("estado")
                libro.libro = datos.get('libro')
                libro.prestatario = datos.get("prestatario")
                libro.save()
                print("prestamo guardado")
                return redirect(listarPrestamos)
    else:
        return render(request, 'sin_acceso.html')
    
    context = {
        "formulario": formulario,
    }
    return render(request, "libroInstancia/uc_libro.html", context)

@login_required
def updateLibroInstancia(request, id):
    libro = LibroInstancia.objects.get(libroinstancia_id=id)
    usuario = request.user

    if usuario.groups.filter(name="bibliotecario").exists():
        if request.method == 'POST':
            formulario = FormularioModificarLibro(request.POST)
            if formulario.is_valid():
                datos=formulario.cleaned_data
                libro.fecha_devolucion = datos.get("fecha_devolucion")
                libro.estado = datos.get("estado")
                libro.libro = datos.get('libro')
                libro.prestatario = datos.get("prestatario")
                libro.save()
                return redirect(listarPrestamos)
        else:
            formulario = FormularioModificarLibro(instance=libro)
    else:
        return render(request, 'sin_acceso.html')

    
    context = {
        "formulario": formulario,
    }
    return render(request, "libroInstancia/uc_libro.html", context)
