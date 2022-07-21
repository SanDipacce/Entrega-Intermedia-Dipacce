
from django.contrib import admin
from .models import Proveedores, Productos, Empleados

admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Proveedores)

