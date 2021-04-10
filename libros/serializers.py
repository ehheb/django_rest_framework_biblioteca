from rest_framework.serializers import ModelSerializer
from libros.models import Libro

class LibroSerializer(ModelSerializer):

    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'fecha_publicacion', 'paginas', 'editorial', 'autores')
