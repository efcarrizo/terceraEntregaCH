from django.contrib import admin
from .models import Producto, Empleado, Cliente

# Register your models here.
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Cliente)