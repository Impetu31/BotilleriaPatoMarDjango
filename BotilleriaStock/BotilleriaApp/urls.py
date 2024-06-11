from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ClienteViewSet, MovimientoViewSet, BoletaViewSet, DetalleBoletaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'movimientos', MovimientoViewSet)
router.register(r'boletas', BoletaViewSet)
router.register(r'detalles', DetalleBoletaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
