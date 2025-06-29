from django.contrib import admin
from .models import Warehouse, InventoryLocation, InventoryItem, InventoryTransaction

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_id', 'code', 'name', 'organization', 'is_active', 'created', 'modified')
    search_fields = ('code', 'name', 'organization__name')
    list_filter = ('is_active', 'organization')
    ordering = ('code',)

@admin.register(InventoryLocation)
class InventoryLocationAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'warehouse', 'code', 'name', 'location_type', 'is_active', 'created', 'modified')
    search_fields = ('code', 'name', 'warehouse__code')
    list_filter = ('location_type', 'is_active', 'warehouse')
    ordering = ('warehouse', 'code')

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('inventory_item_id', 'product', 'warehouse', 'location', 'quantity_on_hand', 'unit_cost', 'total_cost', 'organization', 'created', 'modified')
    search_fields = ('product__name', 'warehouse__code', 'location__code')
    list_filter = ('warehouse', 'location', 'organization')
    ordering = ('product',)

@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'transaction_type', 'transaction_date', 'product', 'quantity', 'unit_cost', 'from_warehouse', 'to_warehouse', 'from_location', 'to_location', 'organization', 'created', 'modified')
    search_fields = ('product__name', 'from_warehouse__code', 'to_warehouse__code')
    list_filter = ('transaction_type', 'transaction_date', 'from_warehouse', 'to_warehouse')
    ordering = ('-transaction_date',)
