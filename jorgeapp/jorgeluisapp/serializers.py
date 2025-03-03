from rest_framework import serializers
from .models import Usuario, Perfil, DatosExternosjuan , DatosExternoscris, DatosExternoscamilo, MeteoriteLanding, Trip, Envio

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'
        
class DatosjuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternosjuan
        fields = '__all__'
        
class DatoscrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternoscris
        fields = '__all__'
        
class DatoscamiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternoscamilo
        fields = '__all__'
        
class DatosmeteoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeteoriteLanding
        fields = ['name']
        
class DatosprivakaggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
class DatospublicosleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'
