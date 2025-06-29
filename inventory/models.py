from django.db import models
from usermanagement.models import UserOrganizationMixin
from django_extensions.db.models import TimeStampedModel
from product.models import Product


class Warehouse(UserOrganizationMixin, TimeStampedModel):
    warehouse_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('organization', 'code')

    def __str__(self):
        return f"{self.code} - {self.name}"


class InventoryLocation(UserOrganizationMixin, TimeStampedModel):
    location_id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=50, default='DEFAULT') 
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('warehouse', 'code')

    def __str__(self):
        return f"{self.warehouse.code}/{self.code}"


class InventoryItem(UserOrganizationMixin, TimeStampedModel):
    inventory_item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    location = models.ForeignKey(InventoryLocation, on_delete=models.CASCADE)
    
    quantity_on_hand = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    total_cost = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    class Meta:
        unique_together = ('organization', 'product', 'warehouse', 'location')

    def __str__(self):
        return f"{self.product.name} @ {self.warehouse.code} - {self.location.code}"


class InventoryTransactionType(models.TextChoices):
    IN = 'IN', 'Stock In'
    OUT = 'OUT', 'Stock Out'
    XFER = 'XFER', 'Transfer'
    ADJ = 'ADJ', 'Adjustment'


class InventoryTransaction(UserOrganizationMixin, TimeStampedModel):
    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=10, choices=InventoryTransactionType.choices)
    transaction_date = models.DateField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    from_warehouse = models.ForeignKey(
        Warehouse, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_from'
    )
    to_warehouse = models.ForeignKey(
        Warehouse, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_to'
    )

    from_location = models.ForeignKey(
        InventoryLocation, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_from'
    )
    to_location = models.ForeignKey(
        InventoryLocation, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_to'
    )

    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    journal_id = models.IntegerField(null=True, blank=True)  # Placeholder for GL integration

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} - {self.quantity}"

