from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

from .models import Autor, Libro
from . import forms
# Create your views here.

class Inicio(TemplateView):
    template_name: str = "index.html"

class ListadoAutor(ListView):
    model = Autor
    template_name: str = "libro/autor/listar_autor.html"
    queryset = Autor.objects.filter(estado=True)
    context_object_name = "autores"

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/autor/crear_autor.html"
    form_class = forms.AutorForm
    success_url = reverse_lazy("libro:listar_autor")

class CrearAutor(CreateView):
    model = Autor
    form_class = forms.AutorForm
    template_name = "libro/autor/crear_autor.html"
    success_url = reverse_lazy("libro:listar_autor")

class EliminarAutor(DeleteView):
    model = Autor
    template_name = "libro/autor/autor_confirm_delete.html"

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect("libro:listar_autor")

class ListarLibro(View):
    model = Libro
    form_class = forms.LibroForm
    template_name = "libro/libro/listar_libro.html"

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = {}
        context["object_list"] = self.get_queryset
        context["form"] = self.form_class
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libro:listar_libro")

class CrearLibro(CreateView):
    model = Libro
    form_class = forms.LibroForm
    template_name = "libro/libro/crear_libro.html"
    success_url = reverse_lazy("libro:listar_libro")

class ActualizarLibro(UpdateView):
    model = Libro
    template_name = "libro/libro/listar_libro.html"
    form_class = forms.LibroForm
    success_url = reverse_lazy("libro:listar_libro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.filter(estado=True)
        return context
    

class EliminarLibro(DeleteView):
    model = Libro
    template_name = "libro/libro/libro_confirm_delete.html"

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect("libro:listar_libro")