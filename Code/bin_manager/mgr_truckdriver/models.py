from django.db import models

# Create your models here.


TRIP_STATUS_CHOICES = (
    ('cancelled','CANCELLED'),
    ('scheduled','SCHEDULED'),
    ('completed','COMPLETED'),
)

class Trip(models.Model):
    trip_id = models.IntegerField(db_column='Trip_ID',primary_key=True)  # Field name made lowercase.
    trip_date = models.DateField(db_column='Trip_Date', blank=True, null=True)  # Field name made lowercase.
    route_id = models.IntegerField(db_column='Route_ID', blank=True, null=True)  # Field name made lowercase.
    trip_status =  models.CharField(db_column='Trip_Status', max_length=10, choices=TRIP_STATUS_CHOICES)  # Field name made lowercase.
    truck_id = models.IntegerField(db_column='Truck_ID', blank=True, null=True)  # Field name made lowercase.
    truck_driver_id = models.IntegerField(db_column='Truck_Driver_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trip'