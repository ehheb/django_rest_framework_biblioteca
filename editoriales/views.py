from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer


class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        data = {}
        for key, value in self.request.query_params.items():
            data[key + '__icontains'] = value
        return self.queryset.filter(**data)
