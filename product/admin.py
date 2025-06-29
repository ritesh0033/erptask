from django.contrib import admin
from .models import Product, UoM, ProductUoM


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_code',
        'name',
        'organization',
        'base_uom',
        'costing_method',
        'tracking_method',
        'is_active',
    )
    list_filter = ('organization', 'costing_method', 'tracking_method', 'is_active')
    search_fields = ('name', 'product_code')
    ordering = ('product_code',)


@admin.register(UoM)
class UoMAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'conversion_to_si')
    search_fields = ('code', 'name')
    ordering = ('code',)


@admin.register(ProductUoM)
class ProductUoMAdmin(admin.ModelAdmin):
    list_display = ('product', 'uom', 'factor', 'is_default_sales', 'is_default_purchase')
    list_filter = ('is_default_sales', 'is_default_purchase')
    search_fields = ('product__name', 'uom__code')

