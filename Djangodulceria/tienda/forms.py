from django import forms
from .models import Producto, Role, Usuario, Categoria
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ProductoForm(forms.ModelForm):

    precio = forms.IntegerField(min_value=1, max_value=300000)

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

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]