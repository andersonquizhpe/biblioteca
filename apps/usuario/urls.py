#copiar de archivo  urls.py
from django.urls import path
from . import views

#importar la direccion del metodo
#name ----> unico de cada url
urlpatterns = [
    path('', views.ingresar, name='autenticar'),
    path('logout/', views.cerrar, name='cerrar_sesion'),
]
