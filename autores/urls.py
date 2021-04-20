from rest_framework.routers import DefaultRouter
from autores.views import AutorViewSet

router = DefaultRouter()
router.register(r'', AutorViewSet)
urlpatterns = router.urls

