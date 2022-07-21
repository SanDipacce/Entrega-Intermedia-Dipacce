import email
from django.db import models

class Productos(models.Model):
    marca= models.CharField(max_length=40)
    categoria= models.CharField(max_length=40)
    tipo= models.CharField(max_length=40)
    fecha_Vto = models.DateField()
    precio= models.IntegerField()
    
    def __str__(self):
        return  f"{self.marca} {self.categoria} {self.tipo}"


    
class Empleados(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    dni= models.IntegerField()
    email= models.EmailField()
    
    def __str__(self):
        return  f"{self.dni} {self.nombre} {self.apellido}"
    
class Proveedores(models.Model):
    nombre= models.CharField(max_length=40)
    empresa= models.CharField(max_length=40)
    numero_cliente= models.IntegerField()
    email= models.EmailField()
    
    def __str__(self):
        return  f"{self.empresa} {self.numero_cliente}"
