from rest_framework.serializers import ModelSerializer
from libros.models import Libro
from autores.serializers import AutorSerializer

class LibroSerializer(ModelSerializer):

    autores = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'fecha_publicacion', 'paginas', 'editorial', 'autores')
