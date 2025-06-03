from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_stock, name='lista_stock'),
    path('crear/', views.crear_stock, name='crear_stock'),
    path('editar/<int:pk>/', views.editar_stock, name='editar_stock'),
    path('eliminar/<int:pk>/', views.eliminar_stock, name='eliminar_stock'),
]