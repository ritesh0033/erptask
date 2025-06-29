from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    search_fields = ('name', 'code')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'organization', 'is_staff', 'is_active')
    list_filter = ('organization', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'organization__name')
