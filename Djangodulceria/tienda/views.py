from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Role, Usuario, Categoria
from .forms import ProductoForm,RoleForm, UsuarioForm, CategoriaForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
# Create your views here.

def inicio(request):
    productos = Producto.objects.all()[:3]
    data = {"productos": productos}
    return render(request,'tienda/index.html', data)

# Categoría
@login_required
def agregar_categoria(request):
    data = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoría registrada")
            return redirect(to="listar-categoria")
        else:
            data['form'] = formulario
    return render(request,'tienda/categoria/categoria_add.html', data)

@login_required
def listar_categoria(request):
    busqueda = request.GET.get("buscar")
    categorias = Categoria.objects.all()
    if busqueda:
        categorias = categorias.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    else:
        busqueda = ""
    data = {"categorias": categorias,"busqueda": busqueda}
    return render(request, 'tienda/categoria/categoria_listar.html',data)

@login_required
def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {'form': CategoriaForm(instance=categoria)}

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar-categoria")
        data['form'] = formulario

    return render(request, 'tienda/categoria/categoria_edit.html', data)

@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, "Eliminada correctamente")
    return redirect(to="listar-categoria")

# Producto
def productos(request):
    busqueda = request.GET.get("buscar")
    seleccion = request.GET.get("seleccionar")
    productos = Producto.objects.all()

    if seleccion:
         productos = productos.filter(categoria=seleccion)

    if busqueda:
         productos = productos.filter(
             Q(nombre__icontains=busqueda)
         ).distinct()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(productos,6)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {"entity": productos, "seleccion": seleccion,"busqueda": busqueda,"paginator": paginator}
    return render(request, 'tienda/Vistas/productos.html', data)

@login_required
def agregar_producto(request):
    data = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
            return redirect(to="listar-producto")
        else:
            data['form'] = formulario
    return render(request, 'tienda/producto/agregar.html', data)

@login_required
def listar_producto(request):
    busqueda = request.GET.get("buscar")
    seleccion = request.GET.get("seleccionar")
    productos = Producto.objects.all()

    if seleccion:
        productos = productos.filter(categoria=seleccion)
    
    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    else:
        busqueda = ""
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,6)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {"entity": productos,"busqueda": busqueda,"seleccion": seleccion,"paginator": paginator}
    return render(request, 'tienda/producto/listar.html', data)

@login_required
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {'form': ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar-producto")
        data['form'] = formulario

    return render(request, 'tienda/producto/modificar.html', data)

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar-producto")


# Role
@login_required
def agregar_role(request):
    data = {'form': RoleForm()}
    if request.method == 'POST':
        formulario = RoleForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Rol registrado")
            return redirect(to="listar-role")
        else:
            data['form'] = formulario

    return render(request, 'tienda/rol/role_add.html', data)

@login_required
def listar_role(request):
    busqueda = request.GET.get("buscar")
    lista_roles = Role.objects.all()
    
    if busqueda:
        lista_roles = lista_roles.filter(
            Q(nombre__icontains=busqueda)
        ).distinct()
    else:
        busqueda = ""
    data = {"roles": lista_roles,"busqueda": busqueda}
    return render(request, 'tienda/rol/role_listar.html', data)

@login_required
def modificar_role(request, id):
    role = get_object_or_404(Role, id=id)
    data = {'form': RoleForm(instance=role)}

    if request.method == 'POST':
        formulario = RoleForm(data=request.POST, instance=role)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar-role")
        data['form'] = formulario

    return render(request, 'tienda/rol/role_edit.html', data)

@login_required
def eliminar_role(request, id):
    role = get_object_or_404(Role, id=id)
    role.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar-role")

# Usuario
@login_required
def agregar_user(request):
    data = {'form': UsuarioForm()}
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario registrado")
            return redirect(to="listar-user")
        else:
            data['form'] = formulario

    return render(request, 'tienda/usuario/agregar_user.html', data)

@login_required
def listar_user(request):
    busqueda = request.GET.get("buscar")
    seleccion = request.GET.get("seleccionar")
    usuarios = Usuario.objects.all()

    if seleccion:
        usuarios = usuarios.filter(rol=seleccion)

    if busqueda:
        usuarios = usuarios.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(email__icontains=busqueda) |
            Q(direccion__icontains=busqueda) |
            Q(telefono__icontains=busqueda) |
            Q(rol__nombre__icontains=busqueda)
        ).distinct()
    else:
        busqueda = ""
    
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(usuarios,6)
        usuarios = paginator.page(page)
    except:
        raise Http404
    data = {'entity': usuarios,"seleccion": seleccion,"busqueda": busqueda,"paginator": paginator}
    return render(request, 'tienda/usuario/listar_user.html', data)   

@login_required
def modificar_user(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {'form': UsuarioForm(instance=usuario)}

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar-user")
        data['form'] = formulario

    return render(request, 'tienda/usuario/modificar_user.html', data)
@login_required
def eliminar_user(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar-user")


#Perfil
@login_required
def login_perfil(request):
    return render(request, 'tienda/perfil/perfil.html')

def foro(request):
    return render(request, 'tienda/Vistas/foro.html')

def colaboradores(request):
    return render(request, 'tienda/Vistas/colaboradores.html')

def registro(request):
    data = {'form': CustomUserCreationForm()}

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="index")
        data['form'] = formulario
    return render(request, 'tienda/Vistas/registro.html', data)

def formulario(request):
    return render(request,'tienda/Vistas/formulario.html')

def carrito(request):
    productos = Producto.objects.all()
    total = 0
    for producto in productos:
        total += producto.precio
    iva = total * 0.19
    valor_total = total + iva
    context = {
        'productos': productos,
        'total': total,
        'iva': iva,
        'valor_total': valor_total
    }
    return render(request,'tienda/Vistas/carrito.html')

def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    # Obtener el carrito de la sesión o crear uno si no existe
    carrito = request.session.get('carrito', {})

    # Agregar el producto al carrito o incrementar la cantidad si ya existe
    carrito[producto_id] = carrito.get(producto_id, 0) + 1

    # Actualizar la sesión con el carrito modificado
    request.session['carrito'] = carrito
    return redirect('carrito')