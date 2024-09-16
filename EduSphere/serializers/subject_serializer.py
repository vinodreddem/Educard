from rest_framework import serializers

from Utility.custom_serializer import BaseSerializer
from EduSphere.models import Subject


class SubjectCreateSerializer(BaseSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectListSerializer(BaseSerializer):
    class Meta:
        model = Class
        fields = '__all__'
