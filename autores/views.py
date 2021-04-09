from django.shortcuts import render

from rest_framework import status
from rest_framework.views import Response, APIView
from autores.models import Autor
from autores.serializers import AutorSerializer

class VistaAutor(APIView):
    def get(self, request):
        autores = Autor.objects.all()
        serialized = AutorSerializer(autores, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
    def post(self, request):
        serialized = AutorSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DetalleAutor(APIView):
    def get(self, request, id):
        try:
            autor = Autor.objects.get(id=id)

        except Autor.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = AutorSerializer(autor)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def put(self, request, id):
        try:
            autor = Autor.objects.get(id=id)

        except Autor.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = AutorSerializer(autor, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            autor = Autor.objects.get(id=id)
        except Autor.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = autor.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
