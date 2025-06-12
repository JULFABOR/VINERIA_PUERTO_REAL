from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from Home.models import Clientes
from .forms import ClientesForm


def clientes_page(request):
    return render(request, 'fidelizar_clientes/clientes.html')

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
