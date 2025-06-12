from django.shortcuts import render, redirect
from Home.models import Stocks
from .forms import StocksForm


def lista_stock(request):
    stocks = Stocks.objects.all()
    return render(request, 'manejo_stock/list.html', {'stocks': stocks})


def stock_create(request):
    if request.method == 'POST':
        form = StocksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_stock')
    else:
        form = StocksForm()
    return render(request, 'manejo_stock/form.html', {'form': form, 'titulo': 'Nuevo Movimiento de Stock'})

def stock_update(request, pk):
    stock = get_object_or_404(Stocks, pk=pk)
    form = StocksForm(request.POST or None, instance=stock)
    if form.is_valid():
        form.save()
        return redirect('lista_stock')
    return render(request, 'manejo_stock/form.html', {'form': form, 'titulo': 'Editar Movimiento de Stock'})

def stock_delete(request, pk):
    stock = get_object_or_404(Stocks, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('lista_stock')
    return render(request, 'manejo_stock/confirm_delete.html', {'stock': stock})
