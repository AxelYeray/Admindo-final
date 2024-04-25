
paso 1: primero configure mi entorno virtual usando lo siguiente
python -m venv venv
.venv\Scripts\activate
paso 2: instale django
pip install django
paso 3: inicie el proyecto main usando el siguiente comando
django-admin startproject djangocrud .
paso 4: inicie el servidor local para confirmar que todo esta bien
python manage.py runserver
paso 5: voy a crear una aplicacion llamada tasks usando el comando
python manage.py startapp tasks
agregue tasks a settings INSTALLED_APPS
paso 6: en views agregue 2 funciones home y register
tambien agregue una libreria de django para la creacion de usuarios
from django.contrib.auth.forms import UserCreationForm
y en la funcion register lo Use
def register(request):
    return render(request, "register.html", {"form": UserCreationForm})
    user creationForm es un formulario predeterminado de django y lo guarde en form
    para ese form poder importarlo a un archivo html

lo use en register.html y lo importe con la siguiente sintaxis {{form.as_p}}
y lo guarde dentro de un form porque al parecer se agrega aparte pero si tiene los labels y
cosas correspondientes a un formulario

en ese formulario agregue un boton para enviar la informacion
y dentro del <form> agregue un action="ruta de informacion" y agregue la ruta a donde se envia
la informacion del formulario tambien agregue un method="post" porque nos sirve para 
encriptar la informacion

tambien agregue:
{%% csrf_token %} que evita que alguien suplante nuestra pagina
osea crea un token solamente reconociendo nuestro servidor esto por seguridad
ya que con el method="post" se crea uno pero no es seguro
y con {%% csrf_token %} lo hace seguro


paso 7: en urls agregue un name a las rutas
de esa forma si cambiamos una ruta no debemos modificar mucho
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
]

paso 8: en views.py importe las siguientes bibliotecas
from django.shortcuts import render
Esta biblioteca sirve para renderizar otras paginas como las
html que estoy importando, usando la siguiente sintaxis:

return render(request, "home.html")

from django.http import HttpResponse:
 se utiliza para generar respuestas HTTP para las solicitudes web 
 en aplicaciones Django.

from django.contrib.auth.forms import UserCreationForm
 Esta clase es una forma integrada de Django que facilita la
creación de formularios para el registro de nuevos usuarios en una aplicación web.

from django.contrib.auth.models import User:
El modelo User proporciona campos básicos para representar un usuario en 
una aplicación web, como nombre de usuario, dirección de correo electrónico,
 contraseña, nombre completo, entre otros. Además, incluye métodos y atributos 
 útiles para la gestión de usuarios, como la verificación de contraseñas,
  la generación de tokens de autenticación, y la gestión de permisos y grupos.

En resumen, al importar User, estás obteniendo acceso al modelo de usuario integrado
de Django, lo que te permite trabajar con usuarios dentro de tu aplicación web de 
una manera simplificada y consistente con las prácticas recomendadas de seguridad 
y autenticación.

y lo use de la siguiente manera en la funcion register de views:
user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()

ahora en esa funcion te recarga la pagina si el usuario ya existe
ya que la pagina utiliza una respuesta get y no post ya que solo se validan
datos 
y si se crea un usuario nuevo como es un method post pues ya envia datos a la
base de datos y crea un usuario nuevo

paso 8: en el register.html agregue lo siguiente
{{error}} este error nos da un mensaje si esque en views la funcion register
encuentra que un usuario ya fue creado o si las contraseñas no coinciden, 
tambien vuelve a renderizar el formulario html si es que no coinciden

paso 9: Creamos un archivo tasks.html por el momento solo agregue un h1 que dice tasks
agregue una url.py de tasks
tambien cree la funcion tasks
lo que hago es que en la funcion register una vez que se crea un usuario no existente
redirecciona a tasks, pero antes de eso con la funcion login que pasa el request y el usuario
crea una sesion en el navegador, para poder usar datos de la base de datos de ese usuario.

importe las siguientes librerias para esto:
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError

En particular, IntegrityError se levanta cuando ocurre un problema con la integridad 
de los datos
en la base de datos, como violaciones de restricciones únicas o de clave externa,
cuando se intenta insertar o actualizar datos.

Por ejemplo, si estás intentando insertar un registro en una tabla y
este registro viola una restricción única o una restricción de clave externa,
se lanzará un IntegrityError para informar sobre la violación de la integridad
de los datos.

En resumen, la librería IntegrityError es útil para manejar errores relacionados 
con la integridad de la base de datos en aplicaciones Django.

paso 10: Agregue un archivo llamado base.html que conecta todos los otros archivos html
a ese archivo le agregue un html, le agregue un navbar y aparte un {% block content %} para
asi poder conectar las otras paginas sin tanto problema

paso 11: Agregue una funcion llamada singout  que basicamente lo que hace
es un cierra de sesion para esto usamos la funcion logout que se exporta
from django.contrib.auth import login, logout,
la mando a llamar dentro de la funcion singout  y redirecciono a home

paso 12: cree una funcion llamada signin esta funcion lo que hace
es que si ya existe un usuario creado te permite iniciar sesion y
acceder a datos de ese usuario

paso 13: cree la base de datos usando el orm de django, puse todos los campos
y la cree usando python manage.py makemigrations
python manage.py migrate
luego agregue las siguientes funciones en admin.py para que se pudiera acceder
a las tablas que cree de la base de datos desde el panel administrador

from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Task, TaskAdmin)

paso 14: hice un nuevo archivo llamado create_task.html
este es un formulario que contiene algunos de los campos
creados anteriormente en el archivo models.py contiene el titulo
la description, el precio y si es importante

tambien cree un archivo llamado forms.py que basicamente es el modelo
que contiene los atributos mencionados anteriormente
tambien exporte la siguiente libreria para poder hacerlo
from django.forms import ModelForm
from .models import Task

en ese archivo cree una clase llamada TaskForm y ese formulario lo exporte
en la funcion views.py cuando renderizo el formulario a TaskForm

paso 15: Guardar tareas en la base de datos 
en la funcion create_task lo que hice fue 
form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")

paso 16: Hacer una funcion para listar las tareas osea lo que hice esque cree
la interfaz en el archivo tasks.html  use un for para recorrer las tareas hechas por el
usuario en la base de datos

paso 17: lo que hice fue crear un archivo html llamado task_detail.html
que en este archivo simplemente agregamos un h1 con el nombre del archivo

en urls.py agregamos lo siguiente
path("tasks/<int:task_id>", views.task_detail, name="task_detail"),
en el primer argumento de "tasks/<int:task_id>" despues del / le decimos al
navegador que va a ser un id que lee directamente de la base de datos

en views agregamos lo siguiente
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

   en la variable task se guarda un id, que despues se le pasa al archivo tasks.html
   para que renderize las tareas

   en tasks.html envolvi dentro del li un
    <a href="{% url 'task_detail' task.id %}">
    y pegue lo que ya estaba dentro del li
    </a> 

  esto hace que se renderizen las tareas creadas en la pestaña tasks  

paso 18: modificar una tarea
para esto ocupo el id sacado directamente de la base de datos
tambien valido el usuario que hace la peticion para que solo salgan las tareas
uso el mismo modelo de formulario anteriormente
donde ya se ve una tarea hecha, ya que es la tarea que voy a modificar

tambien modifique el task_detail.html ya que ahí es donde yo renderizo todo

paso 19: borrar una tarea 
primero pasamos a traer la tarea atraves de la base de datos
Luego verificamos si el metodo es POST
uso el metodo delete para borrar la tarea
y redirecciono a tasks


