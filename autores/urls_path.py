from django.urls import path
from autores.views_APIView import VistaAutor, DetalleAutor

#Estas urls ya no se utilizan en el proyecto
#Se dejaron para estudio
app_name = 'autores'

urlpatterns = [
    path('', VistaAutor.as_view()),
    path('<int:id>', DetalleAutor.as_view())
]

#urlpatterns = [
#    path('', AutorGenericViews.as_view()),
#    path('<pk>', AutorDetailGenericViews.as_view())
#]