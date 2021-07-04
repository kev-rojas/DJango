from rest_framework import serializers
from core.models import Obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields =['nombreOb','autor','año', 'tecnica', 'tamaño', 'imagen']