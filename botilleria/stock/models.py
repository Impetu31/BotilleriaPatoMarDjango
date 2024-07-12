from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    rut = models.CharField(max_length=12)  # Corregido a max_length
    numero_documento = models.CharField(max_length=20)  # Corregido a max_length
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario