from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor
from . import forms
from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Inicio(TemplateView):
    template_name: str = "index.html"

class ListadoAutor(ListView):
    model = Autor
    template_name: str = "libro/listar_autor.html"
    queryset = Autor.objects.filter(estado=True)
    context_object_name = "autores"

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/crear_autor.html"
    form_class = forms.AutorForm
    success_url = reverse_lazy("libro:listar_autor")

class CrearAutor(CreateView):
    model = Autor
    form_class = forms.AutorForm
    template_name = "libro/crear_autor.html"
    success_url = reverse_lazy("libro:listar_autor")

class EliminarAutor(DeleteView):
    model = Autor

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect("libro:listar_autor")

def eliminarAutor(request, id):
    try:
        autor = Autor.objects.get(id=id)
        if request.method == "POST":
            autor.estado = False
            autor.save()
            return redirect("libro:listar_autor")
        return render(request, "libro/eliminar_autor.html", {"autor":autor})
    except ObjectDoesNotExist as e:
        error = e
    return render(request, "libro/listar_autor.html", {"error":error})