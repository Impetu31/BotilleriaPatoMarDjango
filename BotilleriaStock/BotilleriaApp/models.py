from django.db import models

# Definición del modelo Producto
class Producto(models.Model):
    sku = models.CharField(primary_key=True, max_length=20, unique=True)
    nombre = models.CharField(max_length=60)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sku} {self.nombre} {self.precio} {self.cantidad}"

# Definición del modelo Cliente
class Cliente(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254)
    rut = models.CharField(max_length=12, primary_key=True, unique=True)
    numero_documento = models.CharField(max_length=6)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre_usuario} {self.correo} {self.rut} {self.numero_documento}"

# Definición del modelo Movimiento
class Movimiento(models.Model):
    TIPO_CHOICES = [('S', 'Salida'), ('E', 'Entrada')]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} {self.cantidad} {self.fecha} {self.cliente}"

# Definición del modelo Boleta
class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetalleBoleta')
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} {self.total}"

# Detalle de Boleta para manejar productos comprados
class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.boleta} {self.producto} {self.cantidad} {self.total}"