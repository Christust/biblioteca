from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"]="form-control"
        self.fields["username"].widget.attrs["placeholder"]="Nombre de usuario"
        self.fields["password"].widget.attrs["class"]="form-control"
        self.fields["password"].widget.attrs["placeholder"]="Contraseña de usuario"

class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de Usuario en la DB

    Variables:
        -password1: Contraseña
        -password2: Verificación de la contraseña
    """
    password1 = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Ingrese su contraseña",
        "id":"password1",
        "required":"required",
    }))
    password2 = forms.CharField(label="Contraseña de confirmación", max_length=50, widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "placeholder":"Ingrese su contraseña",
        "id":"password2",
        "required":"required",
    }))

    class Meta:
        model = Usuario
        fields = ("email", "username", "nombres", "apellidos")
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Email"
                }
            ),
            "nombres": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Nombres"
                }
            ),
            "apellidos": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Apellidos"
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"Username"
                }
            )
        }

    def clean_password2(self):
        """ Validación de contraseña
        Metodo que valida que ambas contraseñas sean iguales, antes de ser encriptadas y guardadas.
        Al fin retorna la contraseña valida.
        Excepciones:
            - ValidationError : Cuando las contraseñas no sean iguales arroja un error.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user 
    
