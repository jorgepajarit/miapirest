from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PerfilViewSet, DatosjuanViewSet, DatoscrisViewSet, DatoscamiloViewSet, DatosmeteoroViewSet, DatosprivakaggleViewSet, DatospublicosViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'Perfil', PerfilViewSet)
router.register(r'Datosjuan', DatosjuanViewSet)
router.register(r'Datoscris', DatoscrisViewSet)
router.register(r'Datoscamilo', DatoscamiloViewSet)
router.register(r'Datosmeteoro', DatosmeteoroViewSet)
router.register(r'Datoskaggle', DatosprivakaggleViewSet)
router.register(r'Datospublicos', DatospublicosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
