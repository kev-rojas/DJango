from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Obra, vehiculo
from .models import Usuario
from .models import Contacto

#crear clase para el formulario desde bd
class vehiculoForm(ModelForm):
    class Meta:
        model=vehiculo
        fields=["patente", "marca", "modelo", "categoria"]

#------------------------------------------------------------------

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ["nombreOb", "autor", "año", "tecnica", "tamaño", "imagen"]

class UsuarioForm(ModelForm):
    class Meta:
        model=Usuario
        fields=["nombre", "email", "contraseña"]

class ContactoFrom(ModelForm):
    class Meta:
        model=Contacto
        fields=["nombre","mensaje"]