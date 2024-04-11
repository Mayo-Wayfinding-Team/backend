# Models for database tables 'Department' and 'Elevators'
# Models were created using djangos automatic model creation. The command for this is below.
# python manage.py inspectdb > models.py

from django.db import models

class Department(models.Model):
    departmentname = models.CharField(db_column='DepartmentName', primary_key=True, max_length=255)
    floor = models.IntegerField(db_column='Floor')  
    closestelevatorname = models.CharField(db_column='ClosestElevatorName',max_length=255, blank=True, null=True) 
    desk = models.CharField(db_column='Desk', max_length=255, blank=True, null=True) 
    closestdoorfloor1 = models.IntegerField(db_column='ClosestDoorFloor1', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department'

class Door(models.Model):
    doornum = models.IntegerField(db_column='DoorNum', primary_key=True)  
    closestparkinglot = models.CharField(db_column='ClosestParkingLot', max_length=255) 

    class Meta:
        managed = False
        db_table = 'Door'

class Elevators(models.Model):
    elevatornum = models.CharField(db_column='ElevatorName', primary_key=True, max_length=255)
    closestdoor = models.IntegerField(db_column='ClosestDoor') 

    class Meta:
        managed = False
        db_table = 'Elevators'