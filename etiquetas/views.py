from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import Response, APIView
from etiquetas.models import Etiqueta
from etiquetas.serializers import EtiquetaSerializer

class VistaEtiqueta(APIView):

    def get(self, request):
        etiquetas = Etiqueta.objects.all()
        serialized = EtiquetaSerializer(etiquetas, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = EtiquetaSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            print(serialized)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

class DetalleEtiqueta(APIView):
    def get(self, request, id):
        try:
            etiqueta = Etiqueta.objects.get(id=id)

        except Etiqueta.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = EtiquetaSerializer(etiqueta)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )


    def put(self, request, id):
        try:
            etiqueta = Etiqueta.objects.get(id=id)

        except Etiqueta.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = EtiquetaSerializer(etiqueta, data=request.data)

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
            etiqueta = Etiqueta.objects.get(id=id)
        except Etiqueta.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = EtiquetaSerializer(
            etiqueta,
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
            etiqueta = Etiqueta.objects.get(id=id)

        except Etiqueta.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = etiqueta.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EtiquetaGenericViews(generics.ListAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

    #sobreescritura de los métodos
    #def get(self, request, *args, **kwargs):
    #    print(request.method)
    #    return super().get(request, *args, **kwargs)


class EtiquetaDetailGenericViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer