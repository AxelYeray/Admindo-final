from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - by " + self.user.username


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - by {self.user.username}"
