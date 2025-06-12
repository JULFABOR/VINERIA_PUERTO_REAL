from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

def proveedores_list(request):
    proveedores = Proveedores.objects.all().values()
    return JsonResponse(list(proveedores), safe=False)

@csrf_exempt
def proveedores_create(request):
    if request.method == 'POST':
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            proveedor = form.save()
            return JsonResponse({'status': 'ok', 'id_prov': proveedor.id_prov})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
def proveedores_update(request, id_prov):
    proveedor = Proveedores.objects.get(pk=id_prov)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
def proveedores_delete(request, id_prov):
    proveedor = Proveedores.objects.get(pk=id_prov)
    if request.method == 'POST':
        proveedor.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

def proveedores_detail(request, id_prov):
    proveedor = Proveedores.objects.get(pk=id_prov)
    data = {
        'id_prov': proveedor.id_prov,
        'name_prov': proveedor.name_prov,
        'registered_name_prov': proveedor.registered_name_prov,
        'phone_prov': proveedor.phone_prov,
        'mail_prov': proveedor.mail_prov,
        'cuit_prov': proveedor.cuit_prov,
        'active_prov': proveedor.active_prov,
    }
    return JsonResponse(data)

def proveedores_page(request):
    return render(request, 'control_compras/proveedores.html')

def clientes_list(request):
    clientes = Clientes.objects.all().values()
    return JsonResponse(list(clientes), safe=False)

@csrf_exempt
def clientes_create(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return JsonResponse({'status': 'ok', 'id_cli': cliente.id_cli})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
def clientes_update(request, id_cli):
    cliente = Clientes.objects.get(pk=id_cli)
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'ok'})
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
def clientes_delete(request, id_cli):
    cliente = Clientes.objects.get(pk=id_cli)
    if request.method == 'POST':
        cliente.delete()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

def clientes_detail(request, id_cli):
    cliente = Clientes.objects.get(pk=id_cli)
    data = {
        'id_cli': cliente.id_cli,
        'name_cli': cliente.name_cli,
        'dni_cli': cliente.dni_cli,
        'mail_cli': cliente.mail_cli,
        'phone_cli': cliente.phone_cli,
        'date_reg_cli': cliente.date_reg_cli.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)

def clientes_page(request):
    return render(request, 'control_compras/clientes.html')