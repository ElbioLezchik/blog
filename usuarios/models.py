from django.db import models
from django.utils import timezone


# Creación de los modelos de la app usuarios.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    foto_perfil = models. FileField()
    descripcion_personal= models.TextField()
    web = models.CharField(max_length= 700, default='DEFAULT VALUE')
    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios'


