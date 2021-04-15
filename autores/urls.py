from django.urls import path
#from autores.views import VistaAutor
#from autores.views import DetalleAutor
from autores.views import AutorGenericViews
from autores.views import AutorDetailGenericViews

app_name = 'autores'

"""urlpatterns = [
    path('', VistaAutor.as_view()),
    path('<int:id>', DetalleAutor.as_view())
]"""

urlpatterns = [
    path('', AutorGenericViews.as_view()),
    path('<pk>', AutorDetailGenericViews.as_view())
]