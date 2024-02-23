from django.db import models

'''
class Department(models.Model):
    department_name = models.CharField(primary_key=True, max_length=255)
    floor = models.IntegerField()
    distance_to_desk = models.FloatField()
    closest_elevator_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_backend_department'


class Elevators(models.Model):
    elevator_num = models.IntegerField(primary_key=True)
    dist_to_door = models.FloatField()

    class Meta:
        managed = False
        db_table = 'django_backend_elevators'
'''

class Department(models.Model):
    departmentname = models.CharField(db_column='DepartmentName', primary_key=True, max_length=255)  # Field name made lowercase.
    floor = models.IntegerField(db_column='Floor')  # Field name made lowercase.
    distancetodesk = models.FloatField(db_column='DistanceToDesk')  # Field name made lowercase.
    closestelevatornum = models.IntegerField(db_column='ClosestElevatorNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'

class Elevators(models.Model):
    elevatornum = models.IntegerField(primary_key=True, db_column='ElevatorNum')  # Field name made lowercase.
    disttodoor = models.FloatField(db_column='DistToDoor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elevators'