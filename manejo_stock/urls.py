from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_stock, name='lista_stock'),
    path('nuevo/', views.stock_create, name='stock_create'),
    path('<int:pk>/editar/', views.stock_update, name='stock_update'),
    path('<int:pk>/eliminar/', views.stock_delete, name='stock_delete'),
]

