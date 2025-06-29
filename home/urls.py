from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SuperuserLoginView, DashboardView, CustomLogoutView

urlpatterns = [
    path('login/', SuperuserLoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
