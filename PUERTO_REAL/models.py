## modelo de base de datos para importar a las apps
from django.db import models

class Provincias(models.Model):
    id_provincias = models.autoincrement = models.auto_field(Primarykey=true)
    nombre_provincia = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_provincia

class ciudades(models.Model):
    id_ciudad = models.auto_increment = models.auto_field(Primarykey=true)
    nombre_ciudad = models.charfield(max_lengeth=100)
    id_provincia = models.foreignkey(provincias, on_delete=models.cascade)
    def __str__(self):
        return self.nombre_ciudad

class calles(models.model):
    id_calle = models.auto_increment = models.auto_field(primarykey=true)
    nombre_calle = models.charfield(max_legenth=100)
    id_ciudad = models.foreinkey(ciudades, on delete=models.cascade)
    def __str__(self):
        return self.nombre_calle

class direcciones (models.model):
    id_direccion = models.auto_increment = models.auto_field(primarykey=true)
    nombre_direccion = models.charfield(max_length=100)
    departamento_direccion = models.charfield(max_length=100)
    referecia_direccion = models.chartfield(max_length=100)
    id_calle = models.foreinkey(calles, on_delete=models.cascade)
    def __str__(self):
        return self.nombre_direccion

#from django.contrib.auth.models import User
class empleados(models.Model):
    id_empleados = models.auto_increment = models.auto_field(primarykey=true)
    nombre_empleado = models.charfield(max_length=100)
    id_direccion = models.foreinkey(direcciones, on_delete=models.cascade)


class roles(models.model):
    id_rol = models.auto_increment = models.auto_field(primarykey=true)
    nombre_rol = models.charfield(max_length=100)
    def __str__(self):
        return self.nombre_rol


class usuario_roles(models.model):
    id_rol = models.auto_increment = models.auto_field(primarykey=true)
    id = models.foreinkey(user, on_delete=models.cascade)
    def __str__(self):
        return self.id_rol

class pedidos_clientes(models.model):
    id_pedido_cli = models.auto_increment = models.auto_field(primarykey=true)
    id = models.foreinkey(user, on delete=models.cascade)
    id_cliente = models.foreinkey(clientes, on delete=models.cascade)
    cantidad_pedido_cli = models.integerfield()
    fecha_pedido_cli = models.datefield()
    def __str__(self):
        return self.id_pedido_cli
