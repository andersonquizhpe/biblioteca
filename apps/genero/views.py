from django.shortcuts import render, redirect
from .forms import FormularioGenero, FormularioModificarGenero
from apps.modelo.models import Genero
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listaGenero(request):
    usuario = request.user
    if usuario.groups.filter(name='administracion'):
        lista = Genero.objects.all().order_by('nombre')
        context = {
            'lista': lista
        }
        return render(request, 'genero/lista.html', context)
    else:
        return render(request, 'sin_acceso.html')

@login_required
def crearGenero(request):
    formulario = FormularioGenero(request.POST)
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
        if request.method == 'POST':
            if formulario.is_valid():
                datos=formulario.cleaned_data
                genero = Genero()
                genero.nombre = datos.get('nombre')
                genero.save()
                return redirect(listaGenero)
    else:
        return render (request, 'sin_acceso.html')
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'genero/uc_genero.html', context)

@login_required
def updateGenero(request):
    generoid= request.GET['id']
    genero = Genero.objects.get(genero_id=generoid)
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
        if request.method == 'POST':
            formulario = FormularioGenero(request.POST)
            if formulario.is_valid():
                datos = formulario.cleaned_data
                genero.nombre = datos.get('nombre')
                genero.save()
                return redirect(listaGenero)
        else:
            formulario = FormularioGenero(instance=genero)
    else:
        return render(request, 'sin_acceso.html')
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'genero/uc_generoE.html', context)

@login_required
def eliminar(request, id):
    usuario = request.user
    if usuario.groups.filter(name='administracion').exists():
        genero =Genero.objects.get(genero_id=id)
        genero.delete()
        return redirect('/genero')
    else:
        return render(request, 'sin_acceso.html')

