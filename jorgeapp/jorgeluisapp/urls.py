from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PerfilViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'Perfil', PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
