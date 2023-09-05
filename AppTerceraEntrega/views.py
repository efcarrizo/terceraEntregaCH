from django.shortcuts import render
from .models import Cliente, Empleado, Producto
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from .forms import *

def cliente(req, nombre, apellido, email):
    
    cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
    cliente.save()
    
    return HttpResponse(f"""
        <p>Nombre cliente: {cliente.nombre} - Apellido Cliente: {cliente.apellido}</p>
    """)
    
def lista_clientes(req):
    
    lista = Cliente.objects.all()
    
    return render(req, "lista_clientes.html", {"lista_clientes": lista})

def inicio(req):
    
    return render(req, "inicio.html")

def clientes(req):
    
    return render(req, 'clientes.html')

def productos(req):
    
    return render(req, 'productos.html')

def empleados(req):
    
    return render(req, 'empleados.html')

def cliente_formulario(req: HttpRequest):
    
    if req.method == 'POST':
        miFormulario = ClienteFormulario(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con éxito"})
        
    else:
        miFormulario = ClienteFormulario()
        
    return render(req, "cliente_formulario.html", {"miFormulario": miFormulario})

def busqueda_cliente(req):
    
    return render(req, "busqueda_cliente.html")

def buscarCliente(req):
    nombre = req.GET.get("nombre")
    
    if nombre:
        try:
            cliente = Cliente.objects.get(nombre=nombre)
            return render(req, "resultado_busqueda_cliente.html", {"cliente": cliente})
        except Cliente.DoesNotExist:
            return HttpResponse(f'No se encontró ningún cliente con el nombre "{nombre}"')
    else:
        return HttpResponse(f'No escribiste ningún nombre')
    
def producto_formulario(req: HttpRequest):
    
    if req.method == 'POST':
        miFormulario = ProductoFormulario(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            producto = Producto(nombre=data["nombre"], codigo=data["codigo"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto creado con éxito"})
        
    else:
        miFormulario = ProductoFormulario()
        
    return render(req, "producto_formulario.html", {"miFormulario": miFormulario})

def busqueda_producto(req):
    
    return render(req, "busqueda_producto.html")

def buscarProducto(req):
    nombre = req.GET.get("nombre")
    
    if nombre:
        try:
            producto = Producto.objects.get(nombre=nombre)
            return render(req, "resultado_busqueda_producto.html", {"producto": producto})
        except Producto.DoesNotExist:
            return HttpResponse(f'No se encontró ningún Producto con el nombre "{nombre}"')
    else:
        return HttpResponse(f'No escribiste ningún nombre')
    
def empleado_formulario(req: HttpRequest):
    
    if req.method == 'POST':
        miFormulario = EmpleadoFormulario(req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], legajo=data["legajo"])
            empleado.save()
            return render(req, "inicio.html", {"mensaje": "Empleado creado con éxito"})
        
    else:
        miFormulario = EmpleadoFormulario()
        
    return render(req, "empleado_formulario.html", {"miFormulario": miFormulario})

def busqueda_empleado(req):
    
    return render(req, "busqueda_empleado.html")

def buscarEmpleado(req):
    nombre = req.GET.get("nombre")
    
    if nombre:
        try:
            empleado = Empleado.objects.get(nombre=nombre)
            return render(req, "resultado_busqueda_empleado.html", {"empleado": empleado})
        except Empleado.DoesNotExist:
            return HttpResponse(f'No se encontró ningún Producto con el nombre "{nombre}"')
    else:
        return HttpResponse(f'No escribiste ningún nombre')