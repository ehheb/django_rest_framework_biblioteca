from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=1000)
