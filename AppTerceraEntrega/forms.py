from django import forms

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    legajo = forms.IntegerField()
    