from rest_framework.routers import DefaultRouter
from libros.views import LibroViewSet


router = DefaultRouter()
router.register(r'', LibroViewSet)
urlpatterns = router.urls


