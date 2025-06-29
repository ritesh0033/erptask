from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = [
        'product_code', 'name', 'base_uom', 'costing_method', 'tracking_method',
        'safety_stock', 'reorder_qty', 'cogs_account_id', 'inventory_account_id', 'is_active'
    ]
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'product_code', 'name', 'base_uom', 'costing_method', 'tracking_method',
        'safety_stock', 'reorder_qty', 'cogs_account_id', 'inventory_account_id', 'is_active'
    ]
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('product_list')
