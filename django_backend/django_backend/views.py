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

def department_names(request):
    department_names = Department.objects.values_list('departmentname', flat=True)
    # Convert queryset to a list
    department_names_list = list(department_names)
    # Return JSON response
    return JsonResponse(department_names_list, safe=False)

'''
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
'''

def get_department(request, department_name):
    try:
        department = Department.objects.get(departmentname=department_name)
        return department
    except Department.DoesNotExist:
        return None

def get_closest_door(request, department_name):
    try:
        department = Department.objects.get(departmentname=department_name)
        
        if department.closestdoorfloor1 is not None:
            closest_door = department.closestdoorfloor1
        else:
            elevator_num = department.closestelevatornum
            elevator = Elevators.objects.get(elevatornum=elevator_num)
            closest_door = elevator.closestdoor
        return closest_door
    except Exception as e:
        return None


def get_closest_parking_lot(request, closest_door):
    try:
        door = Door.objects.get(doornum=closest_door)
        closest_parking_lot_id = door.closestparkinglot
        return closest_parking_lot_id
    except Exception as e:
        return None

def generate_steps(request, department_name):
    try:
        department = get_department(request, department_name)
        closest_door = get_closest_door(request, department_name)
        closest_parking_lot_id = get_closest_parking_lot(request, closest_door)

        steps = []

        if(department.floor == 1):
            steps.append(f'Park in Parking Lot {closest_parking_lot_id}')
            steps.append(f'Enter through door {closest_door}')
            steps.append(f'Check in at desk {department.desk} for your appointment in {department.departmentname}')
        
        if(department.floor == 2):
            steps.append(f'Park in Parking Lot {closest_parking_lot_id}')
            steps.append(f'Enter through door {closest_door}')
            steps.append(f'Walk to elevator {department.closestelevatornum}')
            steps.append(f'Check in at desk {department.desk} for your appointment in {department.departmentname}')

        return JsonResponse({'steps': steps})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

