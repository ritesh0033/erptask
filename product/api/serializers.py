from rest_framework import serializers
from product.models import UoM, Product, ProductUoM


class UoMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UoM
        fields = ['uom_id', 'code', 'name', 'category', 'conversion_to_si']


class ProductSerializer(serializers.ModelSerializer):
    base_uom = UoMSerializer(read_only=True)
    base_uom_id = serializers.PrimaryKeyRelatedField(
        queryset=UoM.objects.all(), source='base_uom', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_code',
            'name',
            'base_uom',
            'base_uom_id',
            'costing_method',
            'tracking_method',
            'safety_stock',
            'reorder_qty',
            'cogs_account_id',
            'inventory_account_id',
            'is_active',
            'organization',
            'created',
            'modified',
        ]
        read_only_fields = ['organization', 'created', 'modified']


class ProductUoMSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    uom = UoMSerializer(read_only=True)
    uom_id = serializers.PrimaryKeyRelatedField(
        queryset=UoM.objects.all(), source='uom', write_only=True
    )

    class Meta:
        model = ProductUoM
        fields = [
            'id',  # default primary key field for this model
            'product',
            'product_id',
            'uom',
            'uom_id',
            'factor',
            'is_default_sales',
            'is_default_purchase',
        ]
