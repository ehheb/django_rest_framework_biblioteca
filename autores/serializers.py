from rest_framework.serializers import ModelSerializer
from autores.models import Autor
#from libros.serializers import LibroSerializer

class AutorSerializer(ModelSerializer):

    #libros = LibroSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'apellido', 'edad', 'telefono', 'libros')
