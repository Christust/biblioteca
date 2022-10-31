from django.contrib import admin
from django.urls import path, include
from apps.libro.views import Inicio
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Inicio.as_view(), name="index"),
    path("libro/", include(("apps.libro.urls", "libro"))),
]
