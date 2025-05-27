from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'control_stock/producto_lista.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'control_stock/producto_detalles.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'control_stock/producto_formulario.html'
    success_url = reverse_lazy('control_stock:producto_lista')

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'control_stock/producto_formulario.html'
    success_url = reverse_lazy('control_stock:producto_lista')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'control_stock/producto_confirmar_eliminacion.html'
    success_url = reverse_lazy('control_stock:producto_lista')

