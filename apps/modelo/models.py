from django.db import models

# Create your models here.
class Editor(models.Model):
    editor_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100, null=False)
    domicilio = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    pais = models.CharField(max_length=100)
    website=models.URLField()

    def _str_(self):
        return self.nombre
	

class Autor(models.Model):
    autor_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, blank=True)

    def _str_(self):
        linea = "%s %s" %(self.nombre, self.apellido)
        return linea

class Libro(models.Model):
    libro_id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    # materia-campo = models.CharField(max_length=100, unique=True, null=False)
    fechaPublicacion = models.DateField(
        auto_now=False, auto_now_add=False, null=False)
    numeroPaginas = models.IntegerField(null=False)
    autor = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="libros", null=True)
    resumen = models.TextField(blank=True)


	
