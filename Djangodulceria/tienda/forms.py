from django import forms
from .models import Producto, Role, Usuario
from django.forms import ModelForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
