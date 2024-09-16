from rest_framework import serializers

from Utility.custom_serializer import BaseSerializer
from EduSphere.models import Class


class ClassCreateSerializer(BaseSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ClassListSerializer(BaseSerializer):
    class Meta:
        model = Class
        fields = '__all__'
