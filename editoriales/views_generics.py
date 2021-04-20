from rest_framework import generics
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer

#Estas vistas ya no se utilizan en el proyecto
#Se dejaron solamente para estudio
class EditorialGenericViews(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class EditorialDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = Editorial