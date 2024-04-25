from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/completed", views.tasks_completed, name="tasks_completed"),
    path("tasks/create", views.create_task, name="create_task"),
    path("tasks/<int:task_id>", views.task_detail, name="task_detail"),
    path("tasks/<int:task_id>/complete", views.complete_task, name="complete_task"),
    path("tasks/<int:task_id>/delete", views.delete_task, name="delete_task"),
    path("logout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/create", views.create_cliente, name="create_cliente"),
    path("clientes/<int:cliente_id>", views.cliente_detail, name="cliente_detail"),
    path("clientes/<int:cliente_id>/complete", views.complete_cliente,name="complete_cliente",),
    path("clientes/<int:cliente_id>/delete", views.delete_cliente, name="delete_cliente"),
    path("clientes/completed", views.clientes_completed, name="clientes_completed")
    
]
