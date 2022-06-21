from django.db import models
from django.utils import timezone


# Creación de los modelos de la app entradas.
class Entradas(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.FileField() 
    slug = models.CharField(max_length=5000)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entradas'


