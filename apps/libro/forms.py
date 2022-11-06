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