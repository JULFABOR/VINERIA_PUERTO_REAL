from django.db import models
from django.utils import timezone

class Proveedores(models.Model):
    id_prov = models.IntegerField(primary_key=True)
    name_prov = models.CharField(max_length=100)
    active_prov = models.BooleanField()
    registered_name_prov = models.CharField(max_length=100)
    phone_prov = models.CharField(max_length=20)
    mail_prov = models.EmailField()
    cuit_prov = models.CharField(max_length=100)

    def __str__(self):
        return self.name_prov

class Productos(models.Model):
    id_prod = models.BigIntegerField(primary_key=True)
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
    id_cli = models.IntegerField(primary_key=True)
    name_cli = models.CharField(max_length=200)
    dni_cli = models.CharField(max_length=100)
    mail_cli = models.EmailField()
    phone_cli = models.CharField(max_length=100)
    date_reg_cli = models.DateField()

    def __str__(self):
        return self.name_cli
    
class Cajas(models.Model):
    id_caja = models.IntegerField(primary_key=True)
    total_gastos_caja = models.DecimalField()
    total_vents_caja = models.DecimalField()
    datetime_open_caja = models.DateTimeField()
    opening_mont_caja = models.DecimalField()
    closing_mont_caja = models.DecimalField()
    open_caja = models.BooleanField()

    def __str__(self):
        return self.open_caja
    
class Compras(models.Model):
    id_comp = models.IntegerField(primary_key =True)
    datetime_comp = models.DateTimeField()
    total_comp = models.DecimalField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.datetime_comp

class Ventas(models.Model):
    id_vent = models.BigIntegerField(primary_key = True)
    total_vent = models.DecimalField()
    datetime_vent = models.DateTimeField()
    cliente = models.ForeignKey(Clientes, on_delete= models.CASCADE)

    def __str__(self):
        return self.id_vent

class Detalle_Compras(models.Model):
    id_det_comp = models.BigIntegerField(primary_key=True)
    cant_det_comp = models.IntegerField()
    subtotal_det_comp = models.DecimalField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtotal_det_comp

class Detalle_Ventas(models.Model):
    id_det_vent = models.BigIntegerField(primary_key=True)
    cant_det_vent = models.IntegerField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)

    def __str__(self):
        return self.cant_det_vent

class Stocks(models.Model):
    id_stock = models.IntegerField(primary_key=True)
    cant_before_stock = models.IntegerField()
    cant_after_stock = models.IntegerField()
    datetime_stock = models.DateTimeField()
    reasonchange_stock = models.CharField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.cant_after_stock

class Alertas (models.Model):
    id_alert = models.IntegerField(primary_key=True)
    message_alert = models.CharField()
    type_alert = models.CharField()
    datetime_alert = models.DateTimeField()
    read_alert = models.BooleanField()

    def __str__(self):
        return self.message_alert
    
class Historial_Stock(models.Model):
    id_histo_stock = models.IntegerField(primary_key=True)
    typemove_histo_stock = models.CharField(max_length=100)
    cantmove_histo_stock = models.CharField(max_length=100)
    reasonmove_histo_stock =models.CharField(max_length=100)
    datetime_histo_stock = models.DateTimeField()
    stock = models.ForeignKey(Stocks, on_delete=models.CASCADE)

    def __str__(self):
        return self.datetime_histo_stock

class Metodos_Pago(models.Model):
    id_metpag = models.IntegerField(primary_key=True)
    name_metpag = models.CharField(max_length=200)

    def __str__(self):
        return self.name_metpag

class Vent_MetPag(models.Model):
    metodopago = models.ForeignKey(Metodos_Pago, on_delete=models.CASCADE,primary_key=True)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE, primary_key=True)
    monto_xvmp = models.DecimalField()

    def __str__(self):
        return self.monto_xvmp

class Pedidos_Clientes(models.Model):
    id_pedi_cli = models.IntegerField(primary_key=True)
    state_pedi_cli = models.CharField(max_length=100)
    date_pedi_cli = models.DateField()
    cantidad_pedido_cli = models.integerfield()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_pedi_cli
    
class Pedidos_Proveedores(models.Model):
    id_pedi_prov = models.IntegerField(primary_key=True)
    state_pedi_prov = models.CharField(max_length=100)
    date_pedi_prov = models.DateField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_pedi_prov

class Detalle_Pedidos_Proveedores(models.Model):
    id_det_ped_prov = models.BigIntegerField(primary_key=True)
    pedido = models.ForeignKey(Pedidos_Proveedores, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_det_ped_prov = models.PositiveIntegerField()
    precio_unitario_det_ped_prov = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} x{self.cantidad}"

class Detalle_Pedidos_Clientes(models.Model):
    id_det_ped_cli = models.BigIntegerField(primary_key=True)    
    pedido = models.ForeignKey(Pedidos_Clientes, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad_det_ped_cli = models.PositiveIntegerField()
    observaciones_det_ped_cli = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.producto} x{self.cantidad}"

class Descuentos(models.Model):
    id_desc = models.BigIntegerField(primary_key=True)
    nombre_desc = models.CharField(max_length=100)
    porcentaje_desc = models.DecimalField(max_digits=5, decimal_places=2)  # Ej: 15.00%
    fecha_inicio_desc = models.DateField()
    fecha_fin_desc = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.porcentaje}%)"

class Producto_En_Descuento(models.Model):
    id_prod_desc = models.BigIntegerField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuentos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto} - {self.descuento}"

class Historial_Precio_Producto(models.Model):
    id_histo_precio_prod = models.BigIntegerField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_anterior_histo_precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nuevo_histo_precio_prod = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} - {self.fecha}"

class Historial_Movimiento_Caja(models.Model):
    id_det_ped_prov = models.BigIntegerField(primary_key=True)
    fecha_histo_movi_caja = models.DateTimeField(auto_now_add=True)
    tipo_histo_movi_caja = models.CharField(max_length=20, choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')])
    montohisto_movi_caja = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_histo_movi_caja = models.TextField()

    def __str__(self):
        return f"{self.tipo} - ${self.monto} ({self.fecha})"

class Prod_Vencido(models.Model):
    id_det_ped_prov = models.BigIntegerField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_venc = models.DateField()
    cantidad_venc = models.PositiveIntegerField()
    motivo_venc = models.CharField(max_length=100, default="Vencimiento")

    def __str__(self):
        return f"{self.producto} - {self.cantidad} vencido(s)"
    
class Puntos_Cliente(models.Model):
    id_det_ped_prov = models.BigIntegerField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    puntos_obtenidos = models.PositiveIntegerField()
    fecha_points = models.DateField(default=timezone.now)

    def _str_(self):
        return f"{self.cliente} ganó {self.puntos_obtenidos} puntos el {self.fecha}"
    
class Provincias(models.Model):
    id_provin = models.autoincrement = models.auto_field(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_provincia

class Ciudades(models.Model):
    id_ciudad = models.auto_increment = models.auto_field(primary_key=True)
    name_ciudad = models.charfield(max_length=100)
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_ciudad

class Calles(models.Model):
    id_calle = models.auto_increment = models.auto_field(primary_key=True)
    name_calle = models.charfield(max_legenth=100)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_calle

class Direcciones (models.Model):
    id_direccion = models.auto_increment = models.auto_field(primary_key=True)
    nombre_direccion = models.charfield(max_length=100)
    departamento_direccion = models.charfield(max_length=100)
    referecia_direccion = models.chartfield(max_length=100)
    calle = models.ForeignKey(Calles, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_direccion

#from django.contrib.auth.models import User
class Empleados(models.Model):
    id_emple = models.auto_increment = models.auto_field(primary_key=True)
    nombre_emple = models.charfield(max_length=100)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_emple

class Roles(models.model):
    id_rol = models.auto_increment = models.auto_field(primary_key=True)
    nombre_rol = models.charfield(max_length=100)

    def __str__(self):
        return self.nombre_rol


class Usuario_Roles(models.model):
    id_rol = models.auto_increment = models.auto_field(primary_key=True)

    def __str__(self):
        return self.id_rol
