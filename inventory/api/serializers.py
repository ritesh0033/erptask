from rest_framework import serializers
from inventory.models import Warehouse, InventoryLocation, InventoryItem, InventoryTransaction


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'warehouse_id', 'code', 'name', 'address', 'is_active', 'organization', 'created', 'modified'
        ]


class InventoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLocation
        fields = [
            'location_id', 'warehouse', 'code', 'name', 'location_type', 'is_active', 'organization', 'created', 'modified'
        ]


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = [
            'inventory_item_id', 'product', 'warehouse', 'location', 'quantity_on_hand', 'unit_cost', 'total_cost', 'organization', 'created', 'modified'
        ]


class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = [
            'transaction_id', 'transaction_type', 'transaction_date', 'product', 
            'from_warehouse', 'to_warehouse', 'from_location', 'to_location', 
            'quantity', 'unit_cost', 'journal_id', 'organization', 'created', 'modified'
        ]
