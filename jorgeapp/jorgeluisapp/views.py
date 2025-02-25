from rest_framework import generics , viewsets
from .models import Usuario, Perfil, DatosExternosjuan, DatosExternoscris , DatosExternoscamilo , MeteoriteLanding
from rest_framework.views import APIView
from rest_framework.response import Response 
import requests
from .serializers import UsuarioSerializer, PerfilSerializer, DatosjuanSerializer, DatoscrisSerializer, DatoscamiloSerializer, DatosmeteoroSerializer

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilListCreate(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    
class DatosjuanListCreate(generics.ListCreateAPIView):
    queryset = DatosExternosjuan.objects.all()
    serializer_class = DatosjuanSerializer

class DatosjuanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatosExternosjuan.objects.all()
    serializer_class = DatosjuanSerializer
    
class DatoscrisListCreate(generics.ListCreateAPIView):
    queryset = DatosExternoscris.objects.all()
    serializer_class = DatosExternoscris

class DatoscrisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatosExternoscris.objects.all()
    serializer_class = DatosExternoscris
    
class DatoscamiloListCreate(generics.ListCreateAPIView):
    queryset = DatosExternoscamilo.objects.all()
    serializer_class = DatosExternoscamilo

class DatoscamiloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatosExternoscamilo.objects.all()
    serializer_class = DatosExternoscamilo


    
class JuanAPIView(APIView):
    def get(self, request):
        url = "http://54.157.69.113:8000/api/"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de juanCastaneda"}, status=500)
            
class CristianAPIView(APIView):
    def get(self, request):
        url = "http://3.19.235.79:8000/api/"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de cristian"}, status=500)
            
class CamiloAPIView(APIView):
    def get(self, request):
        url = "https://taller.imesh.app/materias"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de cristian"}, status=500)
            
class DatosmeteoroViewSet(viewsets.ModelViewSet):
    queryset = MeteoriteLanding.objects.all()
    serializer_class = DatosmeteoroSerializer
            

            

            

            

            

            
            


            

# Create your views here.
