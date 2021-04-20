from editoriales.views import EditorialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', EditorialViewSet)
urlpatterns = router.urls
