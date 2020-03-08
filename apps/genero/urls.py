from django.conf.urls import include, url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('', views.listaGenero, name='genero'),
	path('crearGenero/', views.crearGenero),
	path('modificar/',views.updateGenero),
	path('delete/(?P<id>d+)/$', views.eliminar, name='deleteGenero')  
]
