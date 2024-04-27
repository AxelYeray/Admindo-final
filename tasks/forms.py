from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["nombre", "descripcion", "importante", "total"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Cliente nombre"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            "importante": forms.CheckboxInput(
                attrs={"class": "form-check-input md-auto"}
            ),
            "total": forms.NumberInput(attrs={"class": "form-control"}),
        }
