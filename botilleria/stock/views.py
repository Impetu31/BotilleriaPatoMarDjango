from rest_framework import generics
from .models import Producto, Cliente
from .serializers import ProductoSerializer, ClienteSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        cliente = Cliente.objects.get(nombre_usuario=username)
        
        if cliente.contraseña == password:
            # Autenticación exitosa
            return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso'})
        else:
            # Contraseña incorrecta
            return JsonResponse({'success': False, 'message': 'Credenciales incorrectas'}, status=401)
    except Cliente.DoesNotExist:
        # Usuario no encontrado
        return JsonResponse({'success': False, 'message': 'Credenciales incorrectas'}, status=401)
