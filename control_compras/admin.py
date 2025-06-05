from django.contrib import admin
from Home.models import Productos,Proveedores,Compras,Detalle_Compras,Pedidos_Proveedores,Detalle_Pedidos_Proveedores

admin.site.register(Productos)
admin.site.register(Proveedores)
admin.site.register(Compras)
admin.site.register(Detalle_Compras)
admin.site.register(Pedidos_Proveedores)
admin.site.register(Detalle_Pedidos_Proveedores)
# Register your models here.
