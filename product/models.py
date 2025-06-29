from django.db import models
from usermanagement.models  import UserOrganizationMixin
from django_extensions.db.models import TimeStampedModel


class UoM(models.Model):
    uom_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50) 
    conversion_to_si = models.FloatField() 

    def __str__(self):
        return f"{self.code} ({self.name})"


class ProductCostingMethod(models.TextChoices):
    FIFO = "FIFO", "FIFO"
    AVG = "AVG", "Average"
    STD = "STD", "Standard"


class ProductTrackingMethod(models.TextChoices):
    NONE = "NONE", "None"
    SERIAL = "SERIAL", "Serial"
    BATCH = "BATCH", "Batch"


class Product(UserOrganizationMixin, TimeStampedModel):
    product_id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    base_uom = models.ForeignKey(UoM, on_delete=models.PROTECT, related_name='base_products')
    costing_method = models.CharField(max_length=10, choices=ProductCostingMethod.choices, default=ProductCostingMethod.AVG)
    tracking_method = models.CharField(max_length=10, choices=ProductTrackingMethod.choices, default=ProductTrackingMethod.NONE)
    safety_stock = models.PositiveIntegerField(default=0)
    reorder_qty = models.PositiveIntegerField(default=0)
    cogs_account_id = models.IntegerField(null=True, blank=True)
    inventory_account_id = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        unique_together = ('organization', 'product_code')

    def __str__(self):
        return self.name


class ProductUoM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    uom = models.ForeignKey(UoM, on_delete=models.CASCADE)
    factor = models.FloatField(help_text="Multiply by this to convert to base unit")
    is_default_sales = models.BooleanField(default=False)
    is_default_purchase = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'uom')

    def __str__(self):
        return f"{self.product.name} - {self.uom.code}"
