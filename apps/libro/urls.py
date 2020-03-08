from django.conf.urls import include, url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('', views.listarlibros, name='libros'),
	path('crear/', views.crearLibro),
	path('modificar/',views.actualizarLibro),
	path(r'^getLibro/(?P<id>d+)/$', views.detalle_libro, name='getLibro'),
	path('delete/(?P<id>d+)/$', views.eliminarLibro, name='delete')  
]
#urlpatterns = [
    
	#Detalle de un libro en particular
    #url(r'^books/(\d+)/$', views.detalle_libro, name='detail-book'),
	#url(r'^getLibro/(\d+)/$', login_required(views.detalle_libro), name='libro_detalle'),
    #Crear libros
	#Update Libros
	#url(r'^(?P<pk>\d+)/update-libro$', views.LibroUpdateView.as_view(), name='update'),
	#Delete Libros
	#url(r'^(?P<pk>\d+)/delete-libro$', views.LibroDeleteView.as_view(), name='delete'),
#]