from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Cashier, Store, Check, Sale
from .forms import ItemForm, CashierForm, StoreForm, CheckForm, SaleForm,UserRegisterForm
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def item_list(request):
    items = Item.objects.all()
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'item_list.html', {'items': items, 'form': form})


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'form.html', {'form': form})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'confirm_delete.html', {'item': item})


def cashier_list(request):
    cashiers = Cashier.objects.all()
    form = CashierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cashier_list')
    return render(request, 'cashier_list.html', {'cashiers': cashiers, 'form': form})


def cashier_update(request, pk):
    cashier = get_object_or_404(Cashier, pk=pk)
    form = CashierForm(request.POST or None, instance=cashier)
    if form.is_valid():
        form.save()
        return redirect('cashier_list')
    return render(request, 'form.html', {'form': form})


def cashier_delete(request, pk):
    cashier = get_object_or_404(Cashier, pk=pk)
    if request.method == 'POST':
        cashier.delete()
        return redirect('cashier_list')
    return render(request, 'confirm_delete.html', {'cashier': cashier})


def store_list(request):
    stores = Store.objects.all()
    form = StoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('store_list')
    return render(request, 'store_list.html', {'stores': stores, 'form': form})


def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    form = StoreForm(request.POST or None, instance=store)
    if form.is_valid():
        form.save()
        return redirect('store_list')
    return render(request, 'form.html', {'form': form})


def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store_list')
    return render(request, 'confirm_delete.html', {'store': store})


def check_list(request):
    form = CheckForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('check_list')
    checks = Check.objects.all()
    return render(request, 'check_list.html', {'checks': checks, 'form': form})


def check_update(request, pk):
    check = get_object_or_404(Check, pk=pk)
    form = CheckForm(request.POST or None, instance=check)
    if form.is_valid():
        form.save()
        return redirect('check_list')
    return render(request, 'form.html', {'form': form})


def check_delete(request, pk):
    check = get_object_or_404(Check, pk=pk)
    if request.method == 'POST':
        check.delete()
        return redirect('check_list')
    return render(request, 'confirm_delete.html', {'check': check})


def sale_list(request):
    sales = Sale.objects.all()
    form = SaleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sale_list')
    return render(request, 'sale_list.html', {'sales': sales, 'form': form})


def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    form = SaleForm(request.POST or None, instance=sale)
    if form.is_valid():
        form.save()
        return redirect('sale_list')
    return render(request, 'form.html', {'form': form})


def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'confirm_delete.html', {'sale': sale})


def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/accounts/login/')
    return render(request, 'register.html', {'form': form})
