from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Genero(models.Model):
    genero_id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

    def _str_(self):
        return self.name
	

class Lenguaje(models.Model):
    lenguaje_id = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def _str_(self):
        return self.idioma


class Autor(models.Model):
    autor_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, blank=True)


    class Meta:
        ordering =['apellido', 'nombre']

    def get_absolute_url(self):
        return reverse('autor_detalle', args=[str(self.autor_id)])

    def _str_(self):
        return "%s %s" %(self.nombre, self.apellido)


class Libro(models.Model):
    libro_id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    # materia-campo = models.CharField(max_length=100, unique=True, null=False)
    fechaPublicacion = models.DateField(
        auto_now=False, auto_now_add=False, null=False)
    numeroPaginas = models.IntegerField(null=False)
    nombre_editorial=models.CharField('Editorial',max_length=100, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    descripcion = models.CharField(max_length=1000, help_text="Ingrese una breve descripción del libro")
    #editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero, help_text="Seleccione un genero para este libro")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    imagen = models.ImageField(upload_to="libros", null=True)
    resumen = models.TextField(blank=True)

    def _str_(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('libro_detalle', args=[str(self.libro_id)])

import uuid 
from django.contrib.auth.models import User 

class LibroInstancia(models.Model):
    libroinstancia_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True) 
    fecha_devolucion = models.DateField(null=True, blank=True)
    prestatario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    @property
    def is_overdue(self):
        if self.fecha_devolucion and date.today() > self.fecha_devolucion:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Mantenimiento'),
        ('p', 'En prestamo'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )
    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')
    
    class Meta:
        ordering = ["fecha_devolucion"]
        permissions = (("can_mark_returned", "Set book as returned"),)
        
    def _str_(self):
        return '{0} ({1})'.format(self.libroinstancia_id, self.libro.titulo)
	
