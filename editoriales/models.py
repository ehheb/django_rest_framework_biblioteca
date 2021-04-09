from django.db import models


class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=200)
