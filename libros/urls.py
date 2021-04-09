from django.urls import path
from libros.views import VistaLibro
from libros.views import DetalleLibro

app_name = 'libros'
urlpatterns = [
    path('', VistaLibro.as_view()),
    path('<int:id>', DetalleLibro.as_view())
]
