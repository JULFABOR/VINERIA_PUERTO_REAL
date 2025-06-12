from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes_page, name='clientes_page'),
    path('clientes/list/', views.clientes_list, name='clientes_list'),
    path('clientes/create/', views.clientes_create, name='clientes_create'),
    path('clientes/<int:id_cli>/update/', views.clientes_update, name='clientes_update'),
    path('clientes/<int:id_cli>/delete/', views.clientes_delete, name='clientes_delete'),
    path('clientes/<int:id_cli>/detail/', views.clientes_detail, name='clientes_detail'),
]
