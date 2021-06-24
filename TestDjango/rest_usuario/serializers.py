from rest_framework import serializers
from core.models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['nombre','email','contraseña']