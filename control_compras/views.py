from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from Home.models import Productos, Proveedores, Compras, Detalle_Compras, Pedidos_Proveedores, Detalle_Pedidos_Proveedores
from .forms import ProductosForm, ProveedoresForm, Detalle_ComprasForm, Pedidos_ProveedoresForm, Detalle_Pedidos_ProveedoresForm

def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
            form = ProductosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_productos')
            else: 
                form = ProductosForm()
            return render(request, 'productos/form.html', {'form': form, 'titulo': 'Nuevo Producto'})

def producto_update(request, id_prod):
    producto = get_object_or_404(Productos, pk=id_prod)
    form = ProductosForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('lista_productos')
    return render(request, 'productos/form.html', {'form': form})

def producto_delete(request, id_prod):
    producto = get_object_or_404(Productos, pk=id_prod)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirm_delete.html', {'producto': producto})