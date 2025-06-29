from django.urls import path
from .views import (
    OrganizationListCreateAPIView, OrganizationDetailAPIView,
    CustomUserListCreateAPIView, CustomUserDetailAPIView,
)

urlpatterns = [
    # Organization URLs
    path('/organizations/', OrganizationListCreateAPIView.as_view(), name='organization-list-create'),
    path('/organizations/<int:pk>/', OrganizationDetailAPIView.as_view(), name='organization-detail'),

    # CustomUser URLs
    path('/users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('/users/<int:pk>/', CustomUserDetailAPIView.as_view(), name='user-detail'),
]
