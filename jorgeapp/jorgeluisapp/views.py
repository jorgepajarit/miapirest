from rest_framework import generics
from .models import Usuario, perfil
from .serializers import UsuarioSerializer, perfilSerializer

class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class perfilListCreate(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = perfilSerializer

class perfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = perfilSerializer

# Create your views here.
