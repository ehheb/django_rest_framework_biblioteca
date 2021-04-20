from django.urls import path

from editoriales.views_APIView import VistaEditorial, DetalleEditorial

#Estas urls ya no se utilizan en el proyecto
#Se dejaron para estudio
app_name = 'editoriales'

urlpatterns = [
    path('', VistaEditorial.as_view()),
    path('<int:id>', DetalleEditorial.as_view())
]
"""urlpatterns = [

    path('', EditorialGenericViews.as_view()),
    path('<pk>', EditorialDetailGenericViews.as_view())
]"""