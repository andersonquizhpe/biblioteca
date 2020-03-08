from django.shortcuts import render, redirect
from .forms import FormularioGenero, FormularioModificarGenero
from apps.modelo.models import Genero

# Create your views here.
def listaGenero(request):
    lista = Genero.objects.all().order_by('nombre')
    context = {
        'lista': lista
    }
    return render(request, 'genero/lista.html', context)

def crearGenero(request):
    formulario = FormularioGenero(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos=formulario.cleaned_data
            genero = Genero()
            genero.nombre = datos.get('nombre')
            genero.save()
            return redirect(listaGenero)
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'genero/uc_genero.html', context)

def updateGenero(request):
    generoid= request.GET['id']
    genero = Genero.objects.get(genero_id=generoid)

    if request.method == 'POST':
        formulario = FormularioGenero(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            genero.nombre = datos.get('nombre')
            genero.save()
            return redirect(listaGenero)
    else:
        formulario = FormularioGenero(instance=genero)
    
    context = {
        'formulario': formulario,
    }
    return render(request, 'genero/uc_generoE.html', context)

def eliminar(request, id):
    autor =Genero.objects.get(genero_id=id)
    autor.delete()
    return redirect('/genero')

