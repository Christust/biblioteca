from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Funciones para login y logout
from django.contrib.auth.views import logout_then_login, LoginView
from apps.libro.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio", login_required(Inicio.as_view()), name="index"),
    path("libro/", include(("apps.libro.urls", "libro"))),
    # LoginView con el parametro template_name para dirigir el login a ese template.
    path("", LoginView.as_view(template_name='login.html', redirect_authenticated_user=True) , name="login"),
    path("logout/", logout_then_login, name="logout")
]
