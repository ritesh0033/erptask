# usermanagement/urls.py

from django.urls import path
from .views import (
    OrganizationListView,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,
)

urlpatterns = [
    path('', OrganizationListView.as_view(), name='organization_list'),
    path('create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('<int:pk>/edit/', OrganizationUpdateView.as_view(), name='organization_edit'),
    path('<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization_delete'),
]
