from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Role, Usuario
from .forms import ProductoForm,RoleForm, UsuarioForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    productos = Producto.objects.all()[:3]
    data = {"productos": productos}
    return render(request,'tienda/index.html', data)
# Producto
def productos(request):
    
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request,'tienda/Vistas/productos.html', data)

def agregar_producto(request):
    data = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario
    return render(request, 'tienda/producto/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'tienda/producto/listar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto modificado correctamente"
            return redirect(to="listar-producto")
        data['form'] = formulario

    return render(request, 'tienda/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar-producto")


# Role
def agregar_role(request):
    data = {'form': RoleForm()}
    if request.method == 'POST':
        formulario = RoleForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario

    return render(request, 'tienda/rol/role_add.html', data)

def listar_role(request):
    lista_roles = Role.objects.all()
    data = {"roles": lista_roles}
    return render(request, 'tienda/rol/role_listar.html', data)

def modificar_role(request, id):
    role = get_object_or_404(Role, id=id)
    data = {'form': RoleForm(instance=role)}

    if request.method == 'POST':
        formulario = RoleForm(data=request.POST, instance=role)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Rol modificado correctamente"
            return redirect(to="listar-role")
        data['form'] = formulario

    return render(request, 'tienda/rol/role_edit.html', data)

def eliminar_role(request, id):
    role = get_object_or_404(Role, id=id)
    role.delete()
    return redirect(to="listar-role")

# Usuario

def agregar_user(request):
    data = {'form': UsuarioForm()}
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario

    return render(request, 'tienda/usuario/agregar_user.html', data)

def listar_user(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'tienda/usuario/listar_user.html', data)   


def modificar_user(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {'form': UsuarioForm(instance=usuario)}

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario modificado correctamente"
            return redirect(to="listar-user")
        data['form'] = formulario

    return render(request, 'tienda/usuario/modificar_user.html', data)

def eliminar_user(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect(to="listar-user")

# Login
def login(request):
    return render(request, 'tienda/Vistas/login.html')

#Inicio empleado
def login_emp(request):
    return render(request, 'tienda/empleado/inicio_empleado.html')