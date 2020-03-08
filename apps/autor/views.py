from django.shortcuts import render, redirect
from .forms import FormularioAutor, FormularioModificarAutor
from apps.modelo.models import Autor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def listaAutores(request):
    usuario = request.user
    if usuario.groups.filter(name='administracion'):
        lista = Autor.objects.all().order_by('autor_id')
        context = {
            'lista': lista
        }
        return render(request, 'autor/lista.html', context)
    else:
        return render(request, 'sin_acceso.html')

@login_required
def crearAutor(request):
    formulario = FormularioAutor(request.POST)
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
        if request.method == 'POST':
            if formulario.is_valid():
                datos=formulario.cleaned_data
                autor = Autor()
                autor.nombre = datos.get('nombre')
                autor.apellido = datos.get('apellido')
                autor.email = datos.get('email')
                autor.save()
                return redirect(listaAutores)
    else:
        print('no tienes acceso')
        return render(request, 'sin_acceso.html')
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'autor/uc_autor.html', context)

@login_required
def updateAutor(request):
    autorid= request.GET['id']
    autor = Autor.objects.get(autor_id=autorid)
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
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
    else:
        return render(request, 'sin_acceso.html')
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'autor/uc_autorE.html', context)

@login_required
def eliminar(request, id):
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
        autor = Autor.objects.get(autor_id=id)
        autor.delete()
        return redirect('/autor')
    else:
        return render(request, 'sin_acceso.html')

