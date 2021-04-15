from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import Response, APIView
from editoriales.models import Editorial
from editoriales.serializers import EditorialSerializer

"""class VistaEditorial(APIView):
    def get(self, request):
        editoriales = Editorial.objects.all()
        serialized = EditorialSerializer(editoriales, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = EditorialSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DetalleEditorial(APIView):
    def get(self, request, id):
        try:
            editorial = Editorial.objects.get(id=id)
        except Editorial.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = EditorialSerializer(editorial)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def put(self, request, id):
        try:
            editorial = Editorial.objects.get(id=id)

        except Editorial.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = EditorialSerializer(editorial, data=request.data)

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
            editorial = Editorial.objects.get(id=id)

        except Editorial.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = editorial.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        """

class EditorialGenericViews(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class EditorialDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = Editorial