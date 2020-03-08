from django.shortcuts import render, redirect
from .forms import FormularioAutor, FormularioModificarAutor
from apps.modelo.models import Autor

# Create your views here.
def listaAutores(request):
    lista = Autor.objects.all().order_by('autor_id')
    context = {
        'lista': lista
    }
    return render(request, 'autor/lista.html', context)

def crearAutor(request):
    formulario = FormularioAutor(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos=formulario.cleaned_data
            autor = Autor()
            autor.nombre = datos.get('nombre')
            autor.apellido = datos.get('apellido')
            autor.email = datos.get('email')
            autor.save()
            return redirect(listaAutores)
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'autor/uc_autor.html', context)

def updateAutor(request):
    autorid= request.GET['id']
    autor = Autor.objects.get(autor_id=autorid)

    if request.method == 'POST':
        formulario = FormularioAutor(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            autor.nombre = datos.get('nombre')
            autor.apellido = datos.get('apellido')
            autor.email = datos.get('email')
            autor.save()
            return redirect(listaAutores)
    else:
        formulario = FormularioAutor(instance=autor)
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'autor/uc_autor.html', context)

def eliminar(request, id):
    autor = Autor.objects.get(autor_id=id)
    autor.delete()
    return redirect('/autor')

