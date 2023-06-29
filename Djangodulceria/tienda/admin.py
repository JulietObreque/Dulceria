from django.contrib import admin
from .models import Categoria,Producto,Role,Usuario
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Role)
admin.site.register(Usuario)

