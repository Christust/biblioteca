from django.contrib import admin
from django.urls import path, include
from apps.libro.views import Home
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home, name="index"),
    path("libro/", include(("apps.libro.urls", "libro"))),
]
