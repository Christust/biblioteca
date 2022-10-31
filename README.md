Iniciamos el proyecto con Django ejecutando:

django-admin startproject <nombre del proyecto>

Si tenemos pipenv dentro del proyecto iniciamos un shell para controlar todos los paquetes:

pipenv shell

Dentro del proyecto tendremos que volver a instalar django para trabajar unicamente con la version que querramos y sus paquetes usando:

pipenv install Django

Todos los comandos pip que necesitemos se correran como pipenv por ejemplo:

pip install <paquete> ---->  pipenv install <paquete>

Si queremos usar algun comando de python como por ejemplo generar un requirements usamos:

pip freeze > requirements.txt ----> pipenv run pip freeze > requirements.txt

Creamos las carpetas <contenedora de las apps> y <templates> en la raiz del proyecto.

Creamos una app dentro de la carpeta de aplicaciones

Modificamos el name dentro de la app en apps.py como:

name = '<carpeta contenedora de apps>.<app>'

Registramos la app en settings.py como:

INSTALLED_APPS = [
    ...
    '<carpeta contenedora de apps>.<app>'
]

Configuramos el lenguaje:

LANGUAGE_CODE = 'es-MX'

Podemos correr las migraciones con:

python3 manage.py makemigrations

python3 manage.py migrate

Y ver nuestro servidor local con:

python3 manage.py runserver

Cuando creamos nuestros modelos podemos registrarlos en el admin para ello podemos personalizar el como se ven usando una Admin Class:

class <nombre del modelo>Admin(admin.ModelAdmin):
...

dentro de esta clase colocamos elementos como barras de busqueda o los elementos con los cuales se tabularan los registros en el admin site:

# Barra de busqueda
search_fields = ["field1", "field2", "field3", ...]

# Listado de campos para tabla
list_display = ("field1", "field2", "field3", ...)

Despues registramos los modelos junto a su admin class todo esto en el admin.py de cada aplicacion:

admin.site.register(<Nombre del modelo>, <Nombre de la clase admin de este modelo>)

En este proyecto se utilizara django_import_export para ello ejecutamos:

pipenv install django-import-export


y luego registramos en settings.py la app de import_export:

# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)

Para usarlo necesitamos dentro de admin.py hacer dos importaciones:

from import_export import resources
from import_export.admin import ImportExportModelAdmin

Despues se crea una clase que herede de resource.ModelResource y en la class Meta colocamos el modelo que lo usara.

class NombreDelModeloResource(resources.ModelResource):
    class Meta:
        model = NombreDelModelo

Finalmente agregamos una herencia mas que es ImportExportModelAdmin y el atributo resource_class el cual es la clase rescource creada anteriormente:

class NombreDelModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    resource_class = NombreDelModeloResource

Para texto enriquecido utilizamos ckeditor. Primero lo descargamos:

pipenv install django-ckeditor

Agremos a las installed_apps:

INSTALLED_APPS = [
    ...
    'ckeditor',
]

Y para usarlo necesitamos en el modelo a aplicar, importar su clase RichTextField y usarlo en el modelo que querramos tener con texto enriquecido:

from ckeditor.fields import RichTextField

class NombreDelModelo(models.Model):
    ...
    campo_con_text_enriquecido = RichTextField()
    ...

Si queremos agregar archivos estaticos necesitamos configurar el settings.py para indicar donde se alojaran estos archivos, en nuestro caso estaran en una carpeta en la base del proyecto:

STATICFILES_DIRS = [
    BASE_DIR / "<nombre de la carpeta contenedora de archivos estaticos>",
]

Si queremos usarlos en nuestros templates debemos incluir al principio de todo la siguiente etiqueta:

{% load static %}

y con esto le indicamos a django que cargue los archivos estaticos y asi consumirlos usando los usemos por ejemplo:

<link
      href="{% static '<path al archivo estatico el cual debe estar en la carpeta declarada anteriormente como la contenedora de archivos estaticos>' %}"
      rel="stylesheet"
    />

Si necesitamos hacer consultas debemos utilizar get_object_or_404 de shortcuts para devolver un 404 en caso de no encontrar el objeto:

from django.shortcuts import render, get_object_or_404

consulta = get_object_or_404(<NombreDelModelo>, field1 = algun_valor)

Si queremos hacer consultas que ignoren mayusculas o minusculas agregamos '__iexact' al parametro que querramos abarcar:

NombreDelModelo.objects.get(field1__iexact="Algun string")

Para desplegar a heroku por ejemplo necesitamos crear una carpeta llamada settings dentro de la carpeta llamada como el proyecto. Ahi crearemos el archivo __init__.py, base.py, local.py y production.py.

En el archivo base.py colocaremos todo el archivo de settings.py menos la configuracion de la base de datos y las variables DEBBUG y ALLOWED_HOSTS y paralelamente en los archivos local y production colocaremos solo esas secciones anteriormente mencionadas.

Instalamos gunicorn:

pipenv install gunicorn

Creamos un archivo Procfile en la base del proyecto y agregamos la siguiente linea:

web: gunicorn <nombre del proyecto>.wsgi

Si hemos creado un pipenv al momento de trabajar el proyecto, para generar el requirements con todo lo necesario para el proyecto podemos usar:

pipenv run pip freeze > requirements.txt

Para crear la app desde heroku cli podemos situarnos en el proyecto y correr:

heroku create <nombre del proyecto sin subguiones>

A su vez debemos agregar heroku a los remotos para poder subirlo con git usando:

heroku git:remote -a <nombre de la app en heroku>

Despues de eso podemos ejecutar:

git push -u heroku master

Si nos aparece un error de staticfiles debemos ejecutar el comando:

heroku config:set DISABLE_COLLECTSTATIC=1

y despues ya podremos volver a corre git push a heroku.

Para configurar postgres colocamos:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': '5432',
    }
}

En production y estos datos los sacamos de heroku en el ad onn de postgres en la seccion de settings y credentials.

Seguido ejecutamos:

heroku run python manage.py makemigrations

heroku run python manage.py migrate


Para servir los archivos estaticos descargamos whitenoise esto para heroku e indicarle quien nos servira los archivos:

pipenv install whitenoise

Agregamos al midleware:

MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]

Posteriormente en el archivo wsgi.py colocamos:

from pathlib import Path
from whitenoise import WhiteNoise

BASE_DIR = Path(__file__).resolve().parent.parent.parent

application = get_wsgi_application()
application = WhiteNoise(application, root=BASE_DIR / "static")


--------------------------------------------------------

Vistas basadas en clases.

Si queremos usar vistas basadas en clases debemos usar desde django.views.generic la clase View:

from django.views.generic import View

Y por ejemplo una vista basada en funciones que renderice un html se podria ver asi:

class NombreDeLaClase(View):
    def get(self, request, *args, **kwargs):
        return render(request, "template.html")

La clase hereda de View y la funcion get especifica que si se utiliza la clase y esta recibe un get se activara dicha funcion, ya no tenemos que verificar mediante if si el request.method es igual a por ejemplo un "GET". Esta funcion recibe por parametros el self, request, *args (si es que se van a utilizar una lista de params), **kwargs (si es que se mandan key-words arguments por los params de la funcion).

Despues se debe registrar la url ahora con la clase y utilizando el metodo as_view() para que funcione correctamente:

from <path a la app>.views import NombreDeLaClase

urlpatterns = [
    ...
    path("<url>", NombreDeLaClase.as_view(), name="<nombre de la url para django>"),
    ...
]

De momentos View es de donde todas las demas clases heredan. Solo es una base.

Cabe destacar que si se necesita solo renderizar un template, la forma correcta seria usar TemplateView el cual es una clase que hereda de View y su funcion es renderizar un template:

from django.views.generic import TemplateView

class NombreDeLaClase(TemplateView):
    template_name: str = "template.html"

En la clase TemplateView solo se necesita modificar el atributo template_name con el nombre del template que se desea renderizar; el ': str' es opcional solo es tipado, el codigo anterior es la forma simplificada de:

class NombreDeLaClase(TemplateView):
    template_name = ""

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

Si queremos una vista basada en clases para listar los registros de un modelo usamos el ListView.

from django.views.generic import ListView

class NombreDeLaClase(ListView):
    model = NombreDelModelo
    template_name: str = "template.html"
    queryset = NombreDelModelo.objects.filter(field1=<alguna condicion>)
    context_object_name = "<nombre del objeto para la plantilla>"

De lo anterior escrito solo model y template_name son necesarios, esto hara que en nuestra plantilla declara en el template_name nos mande un objecto con todos los registros del modelo declarado en model. Si nosotros deseamos un filtrado en esos registros usamos queryset, y opcionalmente si deseamos que el objeto tenga un nombre especifico usamos context_object_name, ya que si no lo declaramos se mandara un objecto con el nombre de object_list a la plantilla.