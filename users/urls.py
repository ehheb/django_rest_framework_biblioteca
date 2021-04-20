from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

routes = DefaultRouter()
routes.register('', UserViewSet)
urlpatterns = routes.urls