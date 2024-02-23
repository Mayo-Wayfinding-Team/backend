from django.shortcuts import render
from rest_framework import generics
from .models import Department, Elevators
from .serializers import DepartmentSerializer, ElevatorsSerializer

def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def elevators_list(request):
    elevators = Elevators.objects.all()
    return render(request, 'elevators_list.html', {'elevators': elevators})

class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ElevatorsListAPIView(generics.ListAPIView):
    queryset = Elevators.objects.all()
    serializer_class = ElevatorsSerializer
