from rest_framework import serializers
from .models import Usuario, Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'
