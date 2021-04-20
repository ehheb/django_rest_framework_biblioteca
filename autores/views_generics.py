from rest_framework import generics
from autores.models import Autor
from autores.serializers import AutorSerializer

#Estas vistas ya no se utilizan en el proyecto
#Se dejaron solamente para estudio
class AutorGenericViews(generics.ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutorDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

