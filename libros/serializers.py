from rest_framework.serializers import ModelSerializer

from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from libros.models import Libro

class LibroSerializer(ModelSerializer):
    editorial = EditorialSerializer()
    autores = AutorSerializer(many=True)
    class Meta:
        model = Libro
        fields = ('id', 'nombre', 'fecha_publicacion', 'paginas', 'editorial', 'autores')


class NuevoLibroSerializer(ModelSerializer):


    class Meta:
        model = Libro
        fields = '__all__'
