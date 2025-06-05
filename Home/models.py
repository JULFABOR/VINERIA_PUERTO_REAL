from django.db import models
from django.utils import timezone

# Create your models here.
class Proveedores(models.Model):
    id_prov = models.AutoField(primary_key=True)
    name_prov = models.CharField(max_length=100)
    active_prov = models.BooleanField()
    registered_name_prov = models.CharField(max_length=100)
    phone_prov = models.CharField(max_length=20)
    mail_prov = models.EmailField()
    cuit_prov = models.CharField(max_length=100)

    def __str__(self):
        return self.name_prov

class Productos(models.Model):
    id_prod = models.AutoField(primary_key=True)
    type_prod = models.CharField(max_length=100)
    dateReg_prod = models.DateField()
    descr_prod = models.CharField(max_length=500)
    brand_prod = models.CharField(max_length=100)
    bar_cod_prod = models.CharField(max_length=50)
    active_prod = models.BooleanField()
    name_prod = models.CharField(max_length=100)
    unitaryprice_prod = models.DecimalField(max_digits=8, decimal_places=2)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_prod

class Clientes(models.Model):
    id_cli = models.AutoField(primary_key=True)
    name_cli = models.CharField(max_length=200)
    dni_cli = models.CharField(max_length=100)
    mail_cli = models.EmailField()
    phone_cli = models.CharField(max_length=100)
    date_reg_cli = models.DateField()

    def __str__(self):
        return self.name_cli
    
class Cajas(models.Model):
    id_caja = models.AutoField(primary_key=True)
    total_gastos_caja = models.DecimalField(max_digits=10, decimal_places=2)
    total_vents_caja = models.DecimalField(max_digits=10, decimal_places=2)
    datetime_open_caja = models.DateTimeField()
    opening_mont_caja = models.DecimalField(max_digits=10, decimal_places=2)
    closing_mont_caja = models.DecimalField(max_digits=10, decimal_places=2)
    open_caja = models.BooleanField()

    def __str__(self):
        return str(self.id_caja)
    
class Compras(models.Model):
    id_comp = models.AutoField(primary_key =True)
    datetime_comp = models.DateTimeField()
    total_comp = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_comp)

class Ventas(models.Model):
    id_vent = models.AutoField(primary_key = True)
    total_vent = models.DecimalField(max_digits=10, decimal_places=2)
    datetime_vent = models.DateTimeField()
    cliente = models.ForeignKey(Clientes, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.id_vent)

class Detalle_Compras(models.Model):
    id_det_comp = models.AutoField(primary_key=True)
    cant_det_comp = models.IntegerField()
    subtotal_det_comp = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_det_comp)

class Detalle_Ventas(models.Model):
    id_det_vent = models.AutoField(primary_key=True)
    cant_det_vent = models.IntegerField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_det_vent)

class Stocks(models.Model):
    id_stock = models.AutoField(primary_key=True)
    cant_before_stock = models.IntegerField()
    cant_after_stock = models.IntegerField()
    datetime_stock = models.DateTimeField()
    reasonchange_stock = models.CharField(max_length=200)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_stock)

class Alertas (models.Model):
    id_alert = models.AutoField(primary_key=True)
    message_alert = models.CharField(max_length=200)
    type_alert = models.CharField(max_length=100)
    datetime_alert = models.DateTimeField()
    read_alert = models.BooleanField()

    def __str__(self):
        return self.message_alert
    
class Historial_Stock(models.Model):
    id_histo_stock = models.AutoField(primary_key=True)
    typemove_histo_stock = models.CharField(max_length=100)
    cantmove_histo_stock = models.CharField(max_length=100)
    reasonmove_histo_stock = models.CharField(max_length=100)
    datetime_histo_stock = models.DateTimeField()
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_histo_stock)

class Metodos_Pago(models.Model):
    id_metpag = models.AutoField(primary_key=True)
    name_metpag = models.CharField(max_length=200)

    def __str__(self):
        return self.name_metpag

class Vent_MetPag(models.Model):
    id = models.AutoField(primary_key=True)
    metodopago = models.ForeignKey(Metodos_Pago, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    monto_xvmp = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

class Pedidos_Clientes(models.Model):
    id_pedi_cli = models.AutoField(primary_key=True)
    state_pedi_cli = models.CharField(max_length=100)
    date_pedi_cli = models.DateField()
    cantidad_pedido_cli = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_pedi_cli
    
class Pedidos_Proveedores(models.Model):
    id_pedi_prov = models.AutoField(primary_key=True)
    state_pedi_prov = models.CharField(max_length=100)
    date_pedi_prov = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_pedi_prov

class Detalle_Pedidos_Proveedores(models.Model):
    id_det_ped_prov = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedidos_Proveedores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_det_ped_prov = models.PositiveIntegerField()
    precio_unitario_det_ped_prov = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} x{self.cantidad_det_ped_prov}"

class Detalle_Pedidos_Clientes(models.Model):
    id_det_ped_cli = models.AutoField(primary_key=True)    
    pedido = models.ForeignKey(Pedidos_Clientes, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_det_ped_cli = models.PositiveIntegerField()
    observaciones_det_ped_cli = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.producto} x{self.cantidad_det_ped_cli}"

class Descuentos(models.Model):
    id_desc = models.AutoField(primary_key=True)
    nombre_desc = models.CharField(max_length=100)
    porcentaje_desc = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 15.00%
    fecha_inicio_desc = models.DateField()
    fecha_fin_desc = models.DateField()

    def __str__(self):
        return f"{self.nombre_desc} ({self.porcentaje_desc}%)"

class Producto_En_Descuento(models.Model):
    id_prod_desc = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuentos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto} - {self.descuento}"

class Historial_Precio_Producto(models.Model):
    id_histo_precio_prod = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_anterior_histo_precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nuevo_histo_precio_prod = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} - {self.fecha}"

class Historial_Movimiento_Caja(models.Model):
    id_histo_movi_caja = models.AutoField(primary_key=True)
    fecha_histo_movi_caja = models.DateTimeField(auto_now_add=True)
    tipo_histo_movi_caja = models.CharField(max_length=20, choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')])
    montohisto_movi_caja = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_histo_movi_caja = models.TextField()

    def __str__(self):
        return f"{self.tipo_histo_movi_caja} - ${self.montohisto_movi_caja} ({self.fecha_histo_movi_caja})"

class Prod_Vencido(models.Model):
    id_prod_venc = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_venc = models.DateField()
    cantidad_venc = models.PositiveIntegerField()
    motivo_venc = models.CharField(max_length=100, default="Vencimiento")

    def __str__(self):
        return f"{self.producto} - {self.cantidad_venc} vencido(s)"
    
class Puntos_Cliente(models.Model):
    id_puntos_cliente = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    puntos_obtenidos = models.PositiveIntegerField()
    fecha_points = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.cliente} ganó {self.puntos_obtenidos} puntos el {self.fecha_points}"
    
class Provincias(models.Model):
    id_provin = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_provincia

class Ciudades(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    name_ciudad = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_ciudad

class Calles(models.Model):
    id_calle = models.AutoField(primary_key=True)
    name_calle = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_calle

class Direcciones (models.Model):
    id_direccion = models.AutoField(primary_key=True)
    nombre_direccion = models.CharField(max_length=100)
    departamento_direccion = models.CharField(max_length=100)
    referecia_direccion = models.CharField(max_length=100)
    calle = models.ForeignKey(Calles, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_direccion

#from django.contrib.auth.models import User
class Empleados(models.Model):
    id_emple = models.AutoField(primary_key=True)
    nombre_emple = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_emple

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol


class Usuario_Roles(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id_usuario_rol)

