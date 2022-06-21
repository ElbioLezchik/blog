from django.db import models
from django.utils import timezone


# Creación de los modelos de la app categorias.
class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    detalles = models.CharField(max_length=500)
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categorias'
