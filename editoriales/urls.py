from django.urls import path
#from editoriales.views import VistaEditorial
#from editoriales.views import DetalleEditorial
from editoriales.views import EditorialGenericViews
from editoriales.views import EditorialDetailGenericViews

app_name = 'editoriales'

"""urlpatterns = [
    path('', VistaEditorial.as_view()),
    path('<int:id>', DetalleEditorial.as_view())
]"""
urlpatterns = [

    path('', EditorialGenericViews.as_view()),
    path('<pk>', EditorialDetailGenericViews.as_view())
]