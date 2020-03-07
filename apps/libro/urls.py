from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views #Le decimos a Django que de este directorio importe el fichero views

urlpatterns = [
    url( r'^$' , views.listarlibros, name='libros' ),
    #Detalle de un libro en particular
    url(r'^books/(\d+)/$', views.detalle_libro, name='detail-book'),
    #Crear libros
	url(r'^crear-libro$', views.LibroCreateView.as_view(), name='crear'),
	#Update Libros
	url(r'^(?P<pk>\d+)/update-libro$', views.LibroUpdateView.as_view(), name='update'),
	#Delete Libros
	url(r'^(?P<pk>\d+)/delete-libro$', views.LibroDeleteView.as_view(), name='delete'),
]