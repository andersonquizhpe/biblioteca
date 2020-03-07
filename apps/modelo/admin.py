from django.contrib import admin
# Register your models here.
from .models import Autor, Genero, Lenguaje, Libro, LibroInstancia

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Lenguaje)
admin.site.register(Libro)
admin.site.register(LibroInstancia)

