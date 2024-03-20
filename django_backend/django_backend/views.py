# Uses templates to render the data from the models

from django.shortcuts import render
from .models import Department, Elevators, Door
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def elevators_list(request):
    elevators = Elevators.objects.all()
    return render(request, 'elevators_list.html', {'elevators': elevators})

def doors_list(request):
    doors = Door.objects.all()
    return render(request, 'door_list.html', {'doors': doors})

def get_steps(request, department_name):
    try:
        department = get_object_or_404(Department, departmentname=department_name)
        closest_door = Door.objects.get(doornum=1)
        closest_parking_lot_id = closest_door.closestparkinglot 
        steps = [
            f'Park in Parking Lot {closest_parking_lot_id}',
            f'Enter through door {closest_door.doornum}',
            f'Check in at desk {department.desk} for your appointment in {department.departmentname}'
        ]
        return JsonResponse({'steps': steps})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
