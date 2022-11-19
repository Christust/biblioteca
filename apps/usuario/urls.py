from django.urls import path
from .views import ListadoUsuario, RegistrarUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("listado_usuario/", login_required(ListadoUsuario.as_view()), name="listar_usuarios"),
    path("registrar_usuario/", login_required(RegistrarUsuario.as_view()), name="registrar_usuario"),
]
