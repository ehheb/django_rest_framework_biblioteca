from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import Response, APIView
from rest_framework.viewsets import ModelViewSet

from autores.models import Autor
from autores.serializers import AutorSerializer
from editoriales.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer, NuevoLibroSerializer

"""class VistaLibro(APIView):

    def get(self, request):
        libros = Libro.objects.all()
        serialized = LibroSerializer(libros, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = LibroSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            print(serialized)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

class DetalleLibro(APIView):
    def get(self, request, id):
        try:
            libro = Libro.objects.get(id=id)

        except Libro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = LibroSerializer(libro)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )


    def put(self, request, id):
        try:
            libro = Libro.objects.get(id=id)

        except Libro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = LibroSerializer(libro, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            libro = Libro.objects.get(id=id)
        except Libro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = LibroSerializer(
            libro,
            data=request.data,
            partial=True
        )

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

    def delete(self, request, id):
        try:
            libro = Libro.objects.get(id=id)

        except Libro.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = libro.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
"""

class LibroGenericViews(generics.ListAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

"""    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NuevoLibroSerializer
        return LibroSerializer"""


class LibroDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        data = {}
        #Libro._meta.get_fields()
        for key, value in self.request.query_params.items():
            if key in ['editorial', 'autores']:
                data[key + '__in'] = value
                continue
            data[key + '__icontains'] = value
        print(data)
        return self.queryset.filter(**data)


        #nombre = self.request.query_params.get('nombre')
        #if nombre:
        #    filtro = self.queryset.filter(nombre__icontains=nombre)
        #    return filtro





    #Método para expandir toda la información si tiene tablas relacionadas
    #def get_serializer_class(self):
    #    if self.request.query_params.get('expand'):
    #        return NuevoLibroSerializer
    #    return LibroSerializer

    #Método para ver que estamos haciendo
    def get_serializer_class(self, *args, **kwargs):
        #if self.action == 'retrieve':
        #    return NuevoLibroSerializer()
        print(self.action)
        return super().get_serializer_class()

    #Acciones
    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def autores(self, request, pk=None):
        libro = self.get_object()

        if request.method == 'GET':
            autores = libro.autores.all()
            serialized = AutorSerializer(autores, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'POST':
            id_autores = request.data['autores']
            for id_autor in id_autores:
                autor = Autor.objects.get(id=id_autor)
                libro.autores.add(autor)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            id_autores = request.data['autores']
            for id_autor in id_autores:
                autor = Autor.objects.get(id=id_autor)
                libro.autores.remove(autor)
            return Response(status=status.HTTP_204_NO_CONTENT)

"""    @action(methods=['GET'], detail=False)
    def ordenar(self, request):
        queryset = self.get_queryset().order_by('-nombre')
        serializer = LibroSerializer(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
"""







"""            if eliminar:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)"""
















"""    @action(methods=['GET'], detail=True)
    def editoral(self, request, pk=None):
        libro = self.get_object()
        serializer = EditorialSerializer(libro.editorial)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
"""