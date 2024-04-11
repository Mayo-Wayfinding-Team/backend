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
            elevator_num = department.closestelevatorname
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

# no start point front end
def generate_steps_nsp(request, department_name):
    try:
        department = get_department(request, department_name)
        closest_door = get_closest_door(request, department_name)
        closest_parking_lot_id = get_closest_parking_lot(request, closest_door)

        steps = []

        if department.floor == 1:
            steps.append(f'Park in Parking Lot {closest_parking_lot_id} and enter through door {closest_door}')
            # steps.append(f'Enter through door {closest_door}')
            steps.append(f'Check in at desk {department.desk} for your appointment in {department.departmentname}')
        else:
            steps.append(f'Park in Parking Lot {closest_parking_lot_id} and enter through door {closest_door}' )
            # steps.append(f'Enter through door {closest_door}')
            steps.append(f'Walk to elevator {department.closestelevatorname} and go to floor {department.floor}')
            steps.append(f'Walk to desk {department.desk}')

        return JsonResponse(steps, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# no start point unity
def unity_steps_nsp(request, department_name):
    try:
        department = get_department(request, department_name)
        closest_door = get_closest_door(request, department_name)
        closest_parking_lot_id = get_closest_parking_lot(request, closest_door)

        unity_steps =  []
        step_pairs = []

        if department.floor == 1:
            scenes = ["Parking", "SpecialtyClinic1"] #TODO: work out logic for telling unity what scene to be on for each step
            unity_steps.append("parking"+str(closest_parking_lot_id))
            unity_steps.append("door"+str(closest_door))
            unity_steps.append("desk"+str(department.desk))
        
        if department.floor == 2:
            scenes = ["Parking", "SpecialtyClinic1","SpecialtyClinic2"] #TODO: work out logic for telling unity what scene to be on for each step
            unity_steps.append("parking"+str(closest_parking_lot_id))
            unity_steps.append("door"+str(closest_door))
            unity_steps.append("elevator"+str(department.closestelevatorname))
            unity_steps.append("desk"+str(department.desk))

        for i in range(len(unity_steps)-1):
            step_pairs.append([scenes[i],unity_steps[i], unity_steps[i+1]])
        
        return JsonResponse(step_pairs, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# department to department front end
def generate_steps_dd(request, start_point, destination):
    try:
        department_sp = get_department(request, start_point)
        department_d = get_department(request, destination)

        steps = []

        if department_sp.floor != department_d.floor:
            steps.append(f'from desk {department_sp.desk} walk to elevator {department_sp.closestelevatorname} and go to floor {department_d.floor}')
            steps.append(f'from elevator {department_d.closestelevatorname} walk to desk {department_d.desk}')
        else:
            steps.append("departments are at the same desk")

        return JsonResponse(steps, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# department to department unity     
def unity_steps_dd(request, start_point, destination):
    try:
        department_sp = get_department(request, start_point) #sp = start point
        department_d = get_department(request, destination) #d = destination

        unity_steps = []
        step_pairs = []

        if department_sp.floor != department_d.floor:
            scenes = ["SpecialtyClinic"+str(department_sp.floor), "SpecialtyClinic"+str(department_d.floor)] #TODO: work out logic for telling unity what scene to be on for each step
            unity_steps.append("desk" + str(department_sp.desk))
            unity_steps.append("elevator" + str(department_sp.closestelevatorname))
            unity_steps.append("desk" + str(department_d.desk))

            for i in range(len(unity_steps)-1):
                step_pairs.append([scenes[i],unity_steps[i], unity_steps[i+1]]) 
        else:
            scenes = ["SpecialtyClinic" + str(department_sp.floor)]
            unity_steps.append("departments are at the same desk")
            
            step_pairs.append([scenes[0], unity_steps[0], unity_steps[0]])

        return JsonResponse(step_pairs, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)