from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important", "price"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Titulo"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            "important": forms.CheckboxInput(
                attrs={"class": "form-check-input md-auto"}
            ),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }
