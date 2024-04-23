from rest_framework import serializers

from Utility.custom_serializer import BaseSerializer
from EduSphere.models import Address


class AddressCreateSerializer(BaseSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressListSerializer(BaseSerializer):
    class Meta:
        model = Address
        fields = '__all__'
