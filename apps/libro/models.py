from email.policy import default
from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    nacionalidad = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    estado = models.BooleanField("Estado", default=True)

    class Meta:
        verbose_name="autor"
        verbose_name_plural = "Autores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 250)
    fecha_publicacion = models.DateField(blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "Libros"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo