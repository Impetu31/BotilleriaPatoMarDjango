from django.urls import path
from .views import ProductoListCreate, ProductoRetrieveUpdateDestroy, ClienteListCreate, ClienteRetrieveUpdateDestroy, login_view

urlpatterns = [
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-detail'),
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroy.as_view(), name='cliente-detail'),
    path('login/', login_view, name='login'),
]
