from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor
from . import forms

# Create your views here.
def Home(request):
    return render(request,"index.html")

def crearAutor(request):
    if request.method == "POST":
        autor_form = forms.AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect("index")
    else:
        autor_form = forms.AutorForm()
    return render(request, "libro/crear_autor.html", {"autor_form":autor_form})

def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request, "libro/listar_autor.html", {"autores":autores})

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