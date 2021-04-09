from django.db import models
from autores.models import Autor
from editoriales.models import Editorial

class Libro(models.Model):
    nombre = models.CharField(max_length=500)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()
    editorial = models.ForeignKey(
        Editorial,
        related_name='libros',
        on_delete=models.SET_NULL,
        null=True
    )
    autores = models.ManyToManyField(Autor, related_name='libros')

