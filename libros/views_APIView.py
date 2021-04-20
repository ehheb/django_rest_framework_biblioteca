from rest_framework import status
from rest_framework.views import APIView, Response
from libros.models import Libro
from libros.serializers import LibroSerializer

#Estas vistas ya no se utilizan en el proyecto
#Se dejaron solamente para estudio
class VistaLibro(APIView):
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
