from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio,name='index'),
    path('productos',views.productos,name='productos'),
    path('agregar-producto',views.agregar_producto, name='agregar-producto'),
    path('listar-producto', views.listar_producto, name='listar-producto'),
    path('modificar-producto/<id>', views.modificar_producto, name='modificar-producto'),
    path('eliminar-producto/<id>', views.eliminar_producto, name='eliminar-producto'),

    path('agregar-role', views.agregar_role, name='agregar-role'),
    path('listar-role', views.listar_role, name='listar-role'),
    path('modificar-role/<id>', views.modificar_role, name='modificar-role'),
    path('eliminar-role/<id>', views.eliminar_role, name='eliminar-role'),

    
    path('agregar-user', views.agregar_user, name='agregar-user'),
    path('listar-user', views.listar_user, name='listar-user'),
    path('modificar-user/<id>', views.modificar_user, name='modificar-user'),
    path('eliminar-user/<id>', views.eliminar_user, name='eliminar-user'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='tienda/Vistas/login.html',next_page='login-emp'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    path('inicio', views.login_emp, name='login-emp'),
]