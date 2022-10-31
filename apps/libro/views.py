from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor
from . import forms
from django.views.generic import TemplateView, View, ListView
# Create your views here.

class Inicio(TemplateView):
    template_name: str = "index.html"

class ListadoAutor(ListView):
    model = Autor
    template_name: str = "libro/listar_autor.html"
    queryset = Autor.objects.filter(estado=True)
    context_object_name = "autores"

def crearAutor(request):
    if request.method == "POST":
        print(request.POST)
        autor_form = forms.AutorForm(request.POST)
        print(autor_form.is_valid())
        if autor_form.is_valid():
            autor_form.save()
            return redirect("index")
    else:
        autor_form = forms.AutorForm()
    return render(request, "libro/crear_autor.html", {"autor_form":autor_form})

def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == "GET":
            autor_form = forms.AutorForm(instance=autor)
        else:
            autor_form = forms.AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect("index")
    except ObjectDoesNotExist as e:
        error = e 
    return render(request, "libro/crear_autor.html", {"autor_form":autor_form, "error": error})

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