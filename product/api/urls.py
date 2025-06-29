from django.urls import path
from .views import (
    UoMListCreateAPIView, UoMDetailAPIView,
    ProductListCreateAPIView, ProductDetailAPIView,
    ProductUoMListCreateAPIView, ProductUoMDetailAPIView,
)

urlpatterns = [
    # UoM endpoints
    path('/uoms/', UoMListCreateAPIView.as_view(), name='uom-list-create'),
    path('/uoms/<int:pk>/', UoMDetailAPIView.as_view(), name='uom-detail'),

    # Product endpoints
    path('/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # ProductUoM endpoints
    path('/product-uoms/', ProductUoMListCreateAPIView.as_view(), name='product-uom-list-create'),
    path('/product-uoms/<int:pk>/', ProductUoMDetailAPIView.as_view(), name='product-uom-detail'),
]
