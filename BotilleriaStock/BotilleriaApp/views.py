from rest_framework import viewsets
from .models import Producto, Cliente, Movimiento, Boleta, DetalleBoleta
from .serializers import ProductoSerializer, ClienteSerializer, MovimientoSerializer, BoletaSerializer, DetalleBoletaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DetalleBoletaViewSet(viewsets.ModelViewSet):
    queryset = DetalleBoleta.objects.all()
    serializer_class = DetalleBoletaSerializer
