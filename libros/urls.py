from django.urls import path
#from libros.views import VistaLibro
#from libros.views import DetalleLibro
from rest_framework.routers import DefaultRouter

from libros.views import LibroGenericViews, LibroViewSet
from libros.views import LibroDetailGenericViews

router = DefaultRouter()
router.register(r'', LibroViewSet)
urlpatterns = router.urls


#app_name = 'libros'

"""urlpatterns = [
    path('', VistaLibro.as_view()),
    path('<int:id>', DetalleLibro.as_view())
]"""

"""urlpatterns = [
    path('', LibroGenericViews.as_view()),
    path('<pk>', LibroDetailGenericViews.as_view())
]
"""