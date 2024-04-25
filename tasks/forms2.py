from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "calle", "colonia", "celular", "folio","important"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "calle": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Calle"}
            ),
            "colonia": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Colonia"}
            ),
            "celular": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Celular"}
            ),
            "folio": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Folio"}
            ),
            "important": forms.CheckboxInput(
                attrs={"class": "form-check-input md-auto"}
            ),
        }