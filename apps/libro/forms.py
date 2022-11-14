from django import forms
from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = ["nombre", "apellido", "nacionalidad", "descripcion"]
        labels = {
            # "atributo" : "texto label para el form"
            "nombre" : "Nombre del autor:",
            "apellido" : "Apellidos del autor:",
            "nacionalidad" : "Nacionalidad del autor:",
            "descripcion" : "Pequeña descripción:",
        }
        widgets = {
            # "atributo" : form.<tipo de dato>
            "nombre" : forms.TextInput(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "Ingrese el nombre del autor",
                }
            ),
            "apellido" : forms.TextInput(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "Ingrese el apellido del autor",
                }
            ),
            "nacionalidad" : forms.TextInput(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "Ingrese la nacionalidad del autor",
                }
            ),
            "descripcion" : forms.Textarea(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "Ingrese la descripción del autor",
                }
            ),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = ["titulo", "autor_id", "fecha_publicacion"]
        labels = {
            # "atributo" : "texto label para el form"
            "titulo" : "Titulo del libro:",
            "autor_id" : "Autores del libro:",
            "fecha_publicacion" : "Fecha de publicación del libro:",
        }
        widgets = {
            # "atributo" : form.<tipo de dato>
            "titulo" : forms.TextInput(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "Ingrese el titulo del libro",
                }
            ),
            "autor_id" : forms.CheckboxSelectMultiple(
                # "atributo" : "valor"
                attrs = {
                    "class" : "",
                }
            ),
            "fecha_publicacion" : forms.SelectDateWidget(
                # "atributo" : "valor"
                attrs = {
                    "class" : "form-control",
                }
            ),
        }