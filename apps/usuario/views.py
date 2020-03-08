from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import FormularioLogin
# Create your views here.


# Create your views here.
def ingresar(request):
    if request.method == 'POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario, password = clave)
            print (user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('libros'))
                else:
                    print ('Usuario desactivado')
            else:
                print('Usuario y/o clave inválida')
    else:
        formulario= FormularioLogin()
    context={
        'formulario': formulario,
    }
    return render (request, 'user/login.html', context)

@login_required
def cerrar(request):
    logout(request)
    return redirect('/')