from rest_framework.serializers import ModelSerializer
from etiquetas.models import Etiqueta

class EtiquetaSerializer(ModelSerializer):

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre', 'descripcion')