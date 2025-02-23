from jorgeluisapp.models import Usuario, Perfil , DatosExternosjuan, DatosExternoscris, DatosExternoscamilo
from rest_framework import viewsets
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    
class DatosjuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternosjuan
        fields = '__all__'
        
class DatosjuanViewSet(viewsets.ModelViewSet):
    queryset = DatosExternosjuan.objects.all()
    serializer_class = DatosjuanSerializer
    
class DatoscrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternoscris
        fields = '__all__'
        
class DatoscrisViewSet(viewsets.ModelViewSet):
    queryset = DatosExternoscris.objects.all()
    serializer_class = DatoscrisSerializer
    
class DatoscamiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosExternoscamilo
        fields = '__all__'
        
class DatoscamiloViewSet(viewsets.ModelViewSet):
    queryset = DatosExternoscamilo.objects.all()
    serializer_class = DatoscamiloSerializer
    
    
    
    
