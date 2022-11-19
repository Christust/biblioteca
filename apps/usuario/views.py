from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from .forms import FormularioLogin, FormularioUsuario
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Usuario
# Create your views here.

class Login(FormView):
    template_name = "login.html"
    form_class = FormularioLogin
    success_url = reverse_lazy("index")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class ListadoUsuario(ListView):
    model = Usuario
    template_name = "usuarios/listar_usuario.html"
    queryset = model.objects.filter(usuario_activo=True)
    
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = "usuarios/crear_usuario.html"
    success_url = reverse_lazy("usuario:listar_usuarios")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data["email"],
                username = form.cleaned_data["username"],
                nombres = form.cleaned_data["nombres"],
                apellidos = form.cleaned_data["apellidos"]
            )
            nuevo_usuario.set_password(form.cleaned_data["password1"])
            nuevo_usuario.save()
            return redirect("usuario:listar_usuarios")
        else:
            return render(request, self.template_name, {"form":form})