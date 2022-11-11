from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "libro"

urlpatterns = [
    path("crear_autor/", login_required(views.CrearAutor.as_view()), name="crear_autor"),
    path("listar_autor", login_required(views.ListadoAutor.as_view()), name="listar_autor"),
    path("editar_autor/<int:pk>", login_required(views.ActualizarAutor.as_view()), name="editar_autor"),
    path("eliminar_autor/<int:pk>", login_required(views.EliminarAutor.as_view()), name="eliminar_autor")
]
