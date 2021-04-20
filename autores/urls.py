from django.urls import path
#from autores.views import VistaAutor
#from autores.views import DetalleAutor
#from autores.views import AutorGenericViews
#from autores.views import AutorDetailGenericViews

#app_name = 'autores'

from rest_framework.routers import DefaultRouter
from autores.views import AutorViewSet

router = DefaultRouter()
router.register(r'', AutorViewSet)
urlpatterns = router.urls

"""urlpatterns = [
    path('', VistaAutor.as_view()),
    path('<int:id>', DetalleAutor.as_view())
]"""

#urlpatterns = [
#    path('', AutorGenericViews.as_view()),
#    path('<pk>', AutorDetailGenericViews.as_view())
#]