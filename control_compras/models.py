from django.db import models
from django.utils import timezone

class Proveedores(models.Model):
    id_prov = models.BigAutoField(primary_key=True, editable=False)
    name_prov = models.CharField(max_length=100)
    active_prov = models.BooleanField()
    registered_name_prov = models.CharField(max_length=100)
    phone_prov = models.CharField(max_length=20)
    mail_prov = models.EmailField()
    cuit_prov = models.CharField(max_length=100)

    class Meta:
        ordering = ['id_prov']
        verbose_name = ['proveedor']
        verbose_name_plural =['proveedores']

    def __str__(self):
        return self.name_prov

class Productos(models.Model):
    id_prod = models.BigAutoField(primary_key=True, editable=False)
    type_prod = models.CharField(max_length=100)
    dateReg_prod = models.DateField()
    descr_prod = models.CharField(max_length=500)
    brand_prod = models.CharField(max_length=100)
    bar_cod_prod = models.CharField(max_length=50)
    active_prod = models.BooleanField()
    name_prod = models.CharField(max_length=100)
    unitaryprice_prod = models.DecimalField(max_digits=8, decimal_places=2)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id_prod']
        verbose_name = ['producto']
        verbose_name_plural =['productos']

    def __str__(self):
        return self.name_prod
    
class Compras(models.Model):
    id_comp = models.BigAutoField(primary_key=True, editable=False)
    datetime_comp = models.DateTimeField()
    total_comp = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id_comp']
        verbose_name = ['compra']
        verbose_name_plural =['compras']

    def __str__(self):
        return f"{self.total_comp},{self.proveedor} el {self.cantidad_det_ped_prov}"
    
class Detalle_Compras(models.Model):
    id_det_comp = models.BigAutoField(primary_key=True, editable=False)
    cant_det_comp = models.IntegerField()
    subtotal_det_comp = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id_det_comp']
        verbose_name = ['detalle_de_compra']
        verbose_name_plural =['detalles_de_compra']

    def __str__(self):
        return f"{self.producto} x {self.cantidad_det_comp} {self.compra}"
    
class Pedidos_Proveedores(models.Model):
    id_pedi_prov = models.BigAutoField(primary_key=True, editable=False)
    state_pedi_prov = models.CharField(max_length=100)
    date_pedi_prov = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id_pedi_prov']
        verbose_name = ['pedido a proveedor']
        verbose_name_plural =['pedidos_a_proveedores']

    def __str__(self):
        return f"{self.date_pedi_prov} x {self.proveedor}"

class Detalle_Pedidos_Proveedores(models.Model):
    id_det_ped_prov = models.BigAutoField(primary_key=True, editable=False)
    pedido = models.ForeignKey(Pedidos_Proveedores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_det_ped_prov = models.PositiveIntegerField()
    precio_unitario_det_ped_prov = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['id_det_ped_prov']
        verbose_name = ['detalle_de_pedido_a_proveedor']
        verbose_name_plural =['detalles_de_pedido_a_proveedores']

    def __str__(self):
        return f"{self.producto} x {self.cantidad_det_ped_prov} x {self.pedido}"