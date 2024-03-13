# Uses templates to render the data from the models

from django.shortcuts import render
from .models import Department, Elevators, Door

def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def elevators_list(request):
    elevators = Elevators.objects.all()
    return render(request, 'elevators_list.html', {'elevators': elevators})

def doors_list(request):
    doors = Door.objects.all()
    return render(request, 'door_list.html', {'doors': doors})



