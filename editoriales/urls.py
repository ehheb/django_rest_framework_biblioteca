from django.urls import path
from editoriales.views import VistaEditorial
from editoriales.views import DetalleEditorial

app_name = 'editoriales'
urlpatterns = [
    path('', VistaEditorial.as_view()),
    path('<int:id>', DetalleEditorial.as_view())
]
