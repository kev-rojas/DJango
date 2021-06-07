from django import forms
from django.forms import ModelForm, fields
from .models import vehiculo
from .models import Usuario

#crear clase para el formulario desde bd
class vehiculoForm(ModelForm):
    class Meta:
        model=vehiculo
        fields=["patente", "marca", "modelo", "categoria"]

#------------------------------------------------------------------

class UsuarioForm(ModelForm):
    class Meta:
        model=Usuario
        fields=["nombre", "email", "contraseña"]