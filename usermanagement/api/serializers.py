from rest_framework import serializers
from usermanagement.models import Organization, CustomUser

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'code']


class CustomUserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), source='organization', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'organization', 'organization_id',
            'is_staff', 'is_active',
        ]
        read_only_fields = ['is_staff', 'is_active']
