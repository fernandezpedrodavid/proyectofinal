from rest_framework import serializers
#
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'password',
            'nombre',
            'tipo_usuario',
            'is_active',
        )
        
        
class UsuarioUpSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    teléfono = serializers.IntegerField()
    email = serializers.EmailField()
    tipo_usuario = serializers.IntegerField()
    
class UsuarioUpSerializer2(serializers.Serializer):
    username = serializers.CharField()


class ActiveUpSerializer(serializers.Serializer):
    is_active = serializers.BooleanField()