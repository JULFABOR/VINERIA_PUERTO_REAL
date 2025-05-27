from django.db import models
from django.utils import timezone 

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha_registro = models.DateField(default=timezone.now)
    descripcion = models.CharField(max_length=500)
    marca = models.CharField(max_length=100)
    codigo_barras = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    ##proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.marca})"