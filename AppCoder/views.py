from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import ProductosFormulario, EmpleadosFormulario, ProveedoresFormulario, ProductosBusqueda
from AppCoder.models import Productos, Empleados, Proveedores

def formulario_Producto(request):  
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data 
            Producto = Productos(marca= informacion['marca'], categoria= informacion['categoria'], tipo= informacion['tipo'],  fecha_Vto= informacion['fecha_Vto'], precio= informacion['precio'] ) ## este  que abre parentesis es del modelo
            Producto.save()
            return render(request, "AppCoder/formulario/productos.html")
    else:  
        miFormulario= ProductosFormulario() 
    return render(request, "AppCoder/formulario/productos.html", {"miFormulario":miFormulario})

def formulario_Empleados(request):  
    if request.method == 'POST':
        miFormulario = EmpleadosFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data 
            Empleado = Empleados(nombre= informacion['nombre'], apellido= informacion['apellido'], dni= informacion['dni'], email = informacion['email']) ## este  que abre parentesis es del modelo
            Empleado.save()
            return render(request, "AppCoder/formulario/empleados.html") 
    else:  
        miFormulario= EmpleadosFormulario()  
    return render(request, "AppCoder/formulario/empleados.html", {"miFormulario":miFormulario})

def formulario_Proveedores(request):  
    if request.method == 'POST':
        miFormulario = ProveedoresFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion= miFormulario.cleaned_data 
            Proveedor = Proveedores(nombre= informacion['nombre'], empresa= informacion['empresa'], numero_cliente= informacion['numero_cliente'], email = informacion['email']) 
            Proveedor.save()
            return render(request, "AppCoder/formulario/proveedores.html") 
    else:  
        miFormulario= ProveedoresFormulario()  
    return render(request, "AppCoder/formulario/proveedores.html", {"miFormulario":miFormulario})

def busquedaProducto(request): 
    busqueda_formulario = ProductosBusqueda()
    if  request.GET:  
        categoria= request.GET['categoria']
        producto= Productos.objects.filter(categoria__icontains= categoria)
        return render(request, "AppCoder/formulario/busqueda_productos_final.html", {"producto":producto, "categoria": categoria})

    
    return render(request, "AppCoder/formulario/busqueda_productos_inicio.html", {"busqueda_formulario":busqueda_formulario})

