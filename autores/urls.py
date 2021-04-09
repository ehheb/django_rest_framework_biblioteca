from django.urls import path
from autores.views import VistaAutor
from autores.views import DetalleAutor

app_name = 'autores'
urlpatterns = [
    path('', VistaAutor.as_view()),
    path('<int:id>', DetalleAutor.as_view())
]