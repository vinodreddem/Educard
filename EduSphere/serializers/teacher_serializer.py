from rest_framework import serializers

from Utility.custom_serializer import BaseSerializer
from EduSphere.models import Teacher


class TeacherCreateSerializer(BaseSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherListSerializer(BaseSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
