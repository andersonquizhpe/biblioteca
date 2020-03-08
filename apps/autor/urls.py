from django.conf.urls import include, url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('', views.listaAutores, name='autor'),
	path('crearAutor/', views.crearAutor), 
    path('modificarAutor/', views.updateAutor),
    path('delete/(?P<id>d+)/$', views.eliminar, name='eliminar')
]