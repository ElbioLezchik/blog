from django.db import models
from django.utils import timezone


# Creación de los modelos de la app categorias.
class DetallesBlog(models.Model):
    detalles = models.CharField(max_length=5000, default='DEFAULT VALUE')
    logo = models.FileField()
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'detallesblog'
