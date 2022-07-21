from django import forms

 
class ProductosFormulario(forms.Form):
    marca= forms.CharField(max_length=40)
    categoria= forms.CharField(max_length=40)
    tipo= forms.CharField(max_length=40)
    fecha_Vto = forms.DateField()
    precio= forms.IntegerField()
    
class EmpleadosFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    dni= forms.IntegerField()
    email= forms.EmailField()
    

class ProveedoresFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    empresa= forms.CharField(max_length=40)
    numero_cliente= forms.IntegerField()
    email= forms.EmailField()
    
class ProductosBusqueda(forms.Form):
    categoria= forms.CharField()
    