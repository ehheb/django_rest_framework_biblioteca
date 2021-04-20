from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from autores.models import Autor
from autores.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            data[key + '__icontains'] = value

        return self.queryset.filter(**data)





