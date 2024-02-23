# Models for database tables 'Department' and 'Elevators'
# Models were created using djangos automatic model creation. The command for this is below.
# python manage.py inspectdb > models.py

from django.db import models

class Department(models.Model):
    departmentname = models.CharField(db_column='DepartmentName', primary_key=True, max_length=255)  
    floor = models.IntegerField(db_column='Floor') 
    distancetodesk = models.FloatField(db_column='DistanceToDesk') 
    closestelevatornum = models.IntegerField(db_column='ClosestElevatorNum', blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'department'

class Elevators(models.Model):
    elevatornum = models.IntegerField(primary_key=True, db_column='ElevatorNum') 
    disttodoor = models.FloatField(db_column='DistToDoor') 

    class Meta:
        managed = False
        db_table = 'elevators'