from django.urls import path
from libros.views_APIView import VistaLibro, DetalleLibro

#Estas urls ya no se utilizan en el proyecto
#Se dejaron para estudio
app_name = 'libros'

urlpatterns = [
    path('', VistaLibro.as_view()),
    path('<int:id>', DetalleLibro.as_view())
]

"""urlpatterns = [
    path('', LibroGenericViews.as_view()),
    path('<pk>', LibroDetailGenericViews.as_view())
]
"""