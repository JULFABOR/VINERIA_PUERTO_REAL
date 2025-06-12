from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
    path('proveedores/', views.proveedores_page, name='proveedores_page'),
    path('proveedores/list/', views.proveedores_list, name='proveedores_list'),
    path('proveedores/create/', views.proveedores_create, name='proveedores_create'),
    path('proveedores/<int:id_prov>/update/', views.proveedores_update, name='proveedores_update'),
    path('proveedores/<int:id_prov>/delete/', views.proveedores_delete, name='proveedores_delete'),
    path('proveedores/<int:id_prov>/detail/', views.proveedores_detail, name='proveedores_detail'),
]