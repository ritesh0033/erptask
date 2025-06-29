from django.urls import path
from .views import (
    WarehouseListCreateAPIView, WarehouseDetailAPIView,
    InventoryLocationListCreateAPIView, InventoryLocationDetailAPIView,
    InventoryItemListCreateAPIView, InventoryItemDetailAPIView,
    InventoryTransactionListCreateAPIView, InventoryTransactionDetailAPIView,
)

urlpatterns = [
    path('/warehouses/', WarehouseListCreateAPIView.as_view(), name='warehouse-list-create'),
    path('/warehouses/<int:pk>/', WarehouseDetailAPIView.as_view(), name='warehouse-detail'),

    path('/inventorylocations/', InventoryLocationListCreateAPIView.as_view(), name='inventorylocation-list-create'),
    path('/inventorylocations/<int:pk>/', InventoryLocationDetailAPIView.as_view(), name='inventorylocation-detail'),

    path('/inventoryitems/', InventoryItemListCreateAPIView.as_view(), name='inventoryitem-list-create'),
    path('/inventoryitems/<int:pk>/', InventoryItemDetailAPIView.as_view(), name='inventoryitem-detail'),

    path('/inventorytransactions/', InventoryTransactionListCreateAPIView.as_view(), name='inventorytransaction-list-create'),
    path('/inventorytransactions/<int:pk>/', InventoryTransactionDetailAPIView.as_view(), name='inventorytransaction-detail'),
]
