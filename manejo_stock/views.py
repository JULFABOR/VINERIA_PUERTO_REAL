from django.shortcuts import render, redirect, get_object_or_404
from Home.models import Stocks
from .forms import StockForm

def lista_stock(request):
    stocks = Stocks.objects.all()
    return render(request, 'manejo_stock/lista_stock.html', {'stocks': stocks})

def crear_stock(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_stock')
    return render(request, 'manejo_stock/form_stock.html', {'form': form})

def editar_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    form = StockForm(request.POST or None, instance=stock)
    if form.is_valid():
        form.save()
        return redirect('lista_stock')
    return render(request, 'manejo_stock/form_stock.html', {'form': form})

def eliminar_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('lista_stock')
    return render(request, 'manejo_stock/eliminar_stock.html', {'stock': stock})