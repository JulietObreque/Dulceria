from django.db import models
from django import forms

# Create your models here.

# Modelo productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=70)
    precio = models.IntegerField()
    cantidad = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to = "productos", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

# Modelo rol
class Role(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

# Modelo usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    rol = models.ForeignKey(Role, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.email
