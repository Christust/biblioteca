from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    nacionalidad = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)