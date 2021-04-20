from rest_framework import generics
from libros.models import Libro
from libros.serializers import LibroSerializer, NuevoLibroSerializer

#Estas vistas ya no se utilizan en el proyecto
#Se dejaron solamente para estudio
class LibroGenericViews(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NuevoLibroSerializer
        return LibroSerializer


class LibroDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
