from django.urls import path
from .views import *

urlpatterns = [
    path('agregar-cliente/<nombre>/<apellido>', cliente, name="AgregarCliente"),
    path('lista_clientes/', lista_clientes, name="Lista_clientes"),
    path('', inicio, name="Inicio"),
    path('clientes/', clientes, name="Clientes"),
    path('productos/', productos,  name="Productos"),
    path('empleados/', empleados, name="Empleados"),
    path('cliente_formulario/', cliente_formulario, name='ClienteFormulario'),
    path('busqueda_cliente/', busqueda_cliente, name="BusquedaCliente"),
    path('buscar_cliente/', buscarCliente, name='BuscarCliente'),
    path('producto_formulario/', producto_formulario, name='ProductoFormulario'),
    path('busqueda_producto/', busqueda_producto, name="BusquedaProducto"),
    path('buscar_producto/', buscarProducto, name='BuscarProducto'),
    path('empleado_formulario/', empleado_formulario, name='EmpleadoFormulario'),
    path('busqueda_empleado/', busqueda_empleado, name="BusquedaEmpleado"),
    path('buscar_empleado/', buscarEmpleado, name='BuscarEmpleado'),

]
