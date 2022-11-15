from dataclasses import field
from rest_framework import serializers
#
from .models import Proyecto, Proyecto_Usuario
from applications.usuario.serializers import UsuarioUpSerializer2

# Serializers para Proyecto
class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'id',
            'nombre',
            'is_active',
        )
        
        
class ProyectoUpSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    

class ActiveUpSerializer(serializers.Serializer):
    is_active = serializers.CharField()
    

#Serializers para Proyecto_Uusarios    
class Proyecto_UsuarioSerializer(serializers.ModelSerializer):
    
    proyecto_id = ProyectoUpSerializer()
    usuario_id = UsuarioUpSerializer2()
    
    class Meta:
        model = Proyecto_Usuario
        fields = (
            'id',
            'proyecto_id',
            'usuario_id',
            'is_active'
        )
    