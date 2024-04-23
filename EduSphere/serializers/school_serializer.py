from rest_framework import serializers

from Utility.custom_serializer import BaseSerializer
from EduSphere.models import School


class SchoolCreateSerializer(BaseSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolListSerializer(BaseSerializer):
    class Meta:
        model = School
        fields = '__all__'
