from django.db import models
from django.urls import reverse
# Create your models here.


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
AccountChoices = [(0,'Customer'),(1,'Driver'),(2,'Admin')]

class Account(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_ID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address_line1 = models.CharField(db_column='Address_Line1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address_line2 = models.CharField(db_column='Address_Line2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact_number = models.IntegerField(db_column='Contact_Number', blank=True, null=True)  # Field name made lowercase.
    user_type_id = models.IntegerField(db_column='User_Type_ID', choices = AccountChoices, default = 0)  # Field name made lowercase.

    class Meta:

        db_table = 'account'

    def __str__(self):
        return str(self.user_id)



class Bin(models.Model):
    bin_id = models.AutoField(db_column='Bin_ID', primary_key=True)  # Field name made lowercase.
    bin_type = models.CharField(db_column='Bin_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bin_weight = models.IntegerField(db_column='Bin_Weight', blank=True, null=True)  # Field name made lowercase.
    class Meta:

        db_table = 'bin'


class Block(models.Model):
    block_id = models.AutoField(db_column='Block_ID', primary_key=True)  # Field name made lowercase.
    block_name = models.CharField(db_column='Block_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    route = models.ForeignKey('Route',on_delete=models.DO_NOTHING,default = 0)  # Field name made lowercase.

    class Meta:

        db_table = 'block'

    def __str__(self):
        return str(self.block_id)

CustomerType = [('Regular','Regular'),('Gold','Gold'),('Platinum','Platinum')]

class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Account',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    block = models.ForeignKey('Block',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    general_bin_qty = models.IntegerField(db_column='bin_general_qty', blank=False, null=False,default = 1)
    recycle_bin_qty = models.IntegerField(db_column='bin_recycle_qty', blank=False, null=False,default = 1)
    compost_bin_qty = models.IntegerField(db_column='bin_compost_qty', blank=False, null=False,default = 1)
    customer_type_id = models.CharField(db_column='User_Type_ID', max_length=32 ,choices = CustomerType, default = 'Regular')  # Field name made lowercase.

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return str(self.customer_id)


class FirstappTopic(models.Model):
    top_name = models.CharField(unique=True, max_length=50)

    class Meta:

        db_table = 'firstapp_topic'


class MessageDetail(models.Model):
    message_id = models.IntegerField(db_column='Message_ID', primary_key=True)  # Field name made lowercase.
    message_description = models.CharField(db_column='Message_Description', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'message_detail'


class NotificationDetail(models.Model):
    notification_id = models.IntegerField(db_column='Notification_ID', primary_key=True)  # Field name made lowercase.
    request_id = models.IntegerField(db_column='Request_ID', blank=True, null=True)  # Field name made lowercase.
    message_id = models.IntegerField(db_column='Message_ID', blank=True, null=True)  # Field name made lowercase.
    notification_type = models.CharField(db_column='Notification_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'notification_detail'

RequestTypeChoices = [('Regular','Regular'),('Priority','Priority')]
RequestStatusChoices = [('New','New'),('In Process','In Process'),('Scheduled','Scheduled'),('Completed','Completed'),('Cancelled','Cancelled')]

class RequestDetail(models.Model):
    request_id = models.AutoField(db_column='Request_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customer',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    trip = models.ForeignKey('Trip',on_delete=models.DO_NOTHING,default=0)  # Field name made lowercase.
    request_type = models.CharField(db_column='Request_Type', max_length=128, choices = RequestTypeChoices, default='Regular')  # Field name made lowercase.
    request_date = models.DateField(db_column='Request_Date', blank=True, null=True)  # Field name made lowercase.
    pickup_date = models.DateField(db_column='Pickup_Date', blank=True, null=True)  # Field name made lowercase.
    request_status = models.CharField(db_column='Request_status', max_length=32, choices = RequestStatusChoices, default = 'New')  # Field name made lowercase.

    class Meta:

        db_table = 'request_detail'


class Route(models.Model):
    route_id = models.AutoField(db_column='Route_ID', primary_key=True)  # Field name made lowercase.
    route_name = models.CharField(db_column='Route_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'route'

    def __str__(self):
        return str(self.route_id)


class Score(models.Model):
    request = models.ForeignKey('RequestDetail',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    request_score = models.FloatField(db_column='Request_Score', blank=True, null=True)  # Field name made lowercase.
    request_distance = models.IntegerField(db_column='Request_Distance', blank=True, null=True)  # Field name made lowercase.
    request_weight = models.IntegerField(db_column='Request_Weight', blank=True, null=True)  # Field name made lowercase.
    request_age = models.IntegerField(db_column='Request_Age', blank=True, null=True)  # Field name made lowercase.
    request_distance_score = models.FloatField(db_column='Request_Distance_Score', blank=True, null=True)  # Field name made lowercase.
    request_weight_score = models.FloatField(db_column='Request_Weight_Score', blank=True, null=True)  # Field name made lowercase.
    request_age_score = models.FloatField(db_column='Request_Age_Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'score'


TRIP_STATUS_CHOICES = (
    ('cancelled','CANCELLED'),
    ('scheduled','SCHEDULED'),
    ('completed','COMPLETED'),

)

class Trip(models.Model):
    trip_id = models.AutoField(db_column='Trip_ID',primary_key=True)  # Field name made lowercase.
    trip_date = models.DateField(db_column='Trip_Date', blank=True, null=True)  # Field name made lowercase.
    route = models.ForeignKey('Route',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    trip_status =  models.CharField(db_column='Trip_Status', max_length=10, choices=TRIP_STATUS_CHOICES)  # Field name made lowercase.
    truck = models.ForeignKey('Truck',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    truck_driver = models.ForeignKey('TruckDriver',on_delete=models.DO_NOTHING)  # Field name made lowercase.

    class Meta:

        db_table = 'trip'


class Truck(models.Model):
    truck_id = models.AutoField(db_column='Truck_ID', primary_key=True)  # Field name made lowercase.
    truck_capacity = models.IntegerField(db_column='Truck_Capacity', blank=True, null=True)  # Field name made lowercase.
    truck_type = models.IntegerField(db_column='Truck_Type', blank=True, null=True)  # Field name made lowercase.
    truck_weight = models.IntegerField(db_column='Truck_Weight', blank=True, null=True)  # Field name made lowercase.
    truck_status = models.CharField(db_column='Truck_Status', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'truck'


class TruckDriver(models.Model):
    truck_driver_id = models.AutoField(db_column='Truck_Driver_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Account',on_delete=models.DO_NOTHING)  # Field name made lowercase.
    driver_status = models.CharField(db_column='Driver_status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    service_hours = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'truck_driver'


class UserType(models.Model):
    user_type_id = models.IntegerField(db_column='User_Type_ID', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='User_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'user_type'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:

        db_table = 'users'

ISSUE_STATUS_CHOICES = (
    ('new','NEW'),
    ('open','OPEN'),
    ('resolved','RESOLVED'),
    ('reopened','REOPENED'),
)

ISSUE_TYPE_CHOICES = (
    ('TRUCK','TRUCK'),
    ('BIN','BIN'),
    ('CUSTOMER-RELATED','CUSTOMER-RELATED'),
    ('OTHER','OTHER')
)

class Issues_Detail(models.Model):
    issue_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    issue_type = models.CharField(db_column='Issue_Type', max_length=32, blank=False, choices=ISSUE_TYPE_CHOICES, default='OTHER')  # Field name made lowercase.
    issue_desc = models.TextField(db_column='Issue_Desc', null=True)  # Field name made lowercase.
    reported_date = models.DateField(db_column='Reported_Date', blank=True, null=True)  # Field name made lowercase.
    issue_status = models.CharField(db_column='Issue_Status', max_length=10, choices=ISSUE_STATUS_CHOICES, default='NEW')  # Field name made lowercase.
    resolved_date = models.DateField(db_column='Resolved_Date', blank=True, null=True)  # Field name made lowercase.
    resolution_desc = models.CharField(db_column='Resolution_Desc', max_length=256, blank=True, null=True)  # Field name made lowercase.
    reported_by = models.IntegerField(db_column='reported_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'issues_detail'
