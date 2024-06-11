from rest_framework import serializers
from .models import Producto, Cliente, Movimiento, Boleta, DetalleBoleta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'precio', 'cantidad']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre_usuario', 'correo', 'rut', 'numero_documento', 'contraseña']

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ['tipo', 'producto', 'cantidad', 'fecha', 'cliente']

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBoleta
        fields = ['boleta', 'producto', 'cantidad', 'total']

class BoletaSerializer(serializers.ModelSerializer):
    detalles = DetalleBoletaSerializer(many=True, read_only=True)

    class Meta:
        model = Boleta
        fields = ['cliente', 'productos', 'total', 'fecha', 'detalles']
