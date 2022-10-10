from django import forms
from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = ["nombre", "apellido", "nacionalidad", "descripcion"]