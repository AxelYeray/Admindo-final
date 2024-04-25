from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .forms2 import ClienteForm
from .models import Task
from .models import Cliente
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def Hello(request):
    return HttpResponse("Hello World!")

@login_required
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": UserCreationForm})
    else:
        
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                return render(
                    request,
                    "register.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        return render(
            request,
            "register.html",
            {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
        )


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, 
        datecompleted__isnull=False).order_by
    ("-datecompleted")
    return render(request, "tasks.html", {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"form": TaskForm, "error": "Los datos son inválidos"},
            )


@login_required
def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {"task": task, "form": form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "task_detail.html",
                {"task": task, "form": form, "error": "Error actualizando tarea"},
            )


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datecompleted = timezone.now()
        task.save()
        return redirect("tasks")


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")


def signout(request):
    logout(request)
    return redirect("signin")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})

    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Usuario y/o contraseña incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("tasks")


@login_required
def clientes(request):
    clientes = Cliente.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "clientes.html", {"clientes": clientes})

@login_required
def clientes_completed(request):
    clientes = Cliente.objects.filter(
        user=request.user, datecompleted__isnull=False
    ).order_by
    ("-datecompleted")
    return render(request, "clientes.html", {"clientes": clientes})


@login_required
def create_cliente(request):
    if request.method == "GET":
        return render(request, "create_cliente.html", {"form": ClienteForm})
    else:
        try:
            form = ClienteForm(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            return redirect("clientes")
        except ValueError:
            return render(
                request,
                "create_cliente.html",
                {"form": ClienteForm, "error": "Los datos son inválidos"},
            )


@login_required
def cliente_detail(request, cliente_id):
    if request.method == "GET":
        cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
        form = ClienteForm(instance=cliente)
        return render(
            request, "cliente_detail.html", {"cliente": cliente, "form": form}
        )
    else:
        try:
            cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
            form = ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect("clientes")
        except ValueError:
            return render(
                request,
                "cliente_detail.html",
                {
                    "cliente": cliente,
                    "form": form,
                    "error": "Error actualizando cliente",
                },
            )

@login_required
def complete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
    if request.method == "POST":
        cliente.datecompleted = timezone.now()
        cliente.save()
        return redirect("clientes")



@login_required
def delete_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id, user=request.user)
    if request.method == "POST":
        cliente.delete()
        return redirect("clientes")




