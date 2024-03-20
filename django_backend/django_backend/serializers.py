# serializers for both models

from rest_framework import serializers
from .models import Department, Elevators

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ElevatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevators
        fields = '__all__'