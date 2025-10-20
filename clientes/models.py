from django.db import models
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre}"
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.nombre
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"
