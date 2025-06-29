from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Warehouse
from django.contrib.auth.mixins import LoginRequiredMixin

class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    template_name = 'inventory/warehouse_list.html'
    context_object_name = 'warehouses'

class WarehouseCreateView(LoginRequiredMixin, CreateView):
    model = Warehouse
    fields = ['code', 'name', 'address', 'is_active']
    template_name = 'inventory/warehouse_form.html'
    success_url = reverse_lazy('warehouse_list')

class WarehouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Warehouse
    fields = ['code', 'name', 'address', 'is_active']
    template_name = 'inventory/warehouse_form.html'
    success_url = reverse_lazy('warehouse_list')

class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warehouse
    template_name = 'inventory/warehouse_confirm_delete.html'
    success_url = reverse_lazy('warehouse_list')

