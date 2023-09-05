from django.db import models

class Cliente(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    legajo = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    

    