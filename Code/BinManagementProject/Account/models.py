from django.db import models

# Create your models here.

"""
class Account (models.Model):

    User_Id = models.CharField(max_length=100,blank=False)
    First_Name = models.CharField(max_length=100,blank=False)
    Last_Name = models.CharField(max_length=100,blank=False)
    Email_Id =  models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=20,blank=False)
    AddressLine1 =models.CharField(max_length=100,blank=False)
    AddressLine2 = models.CharField(max_length=100,default="")
    City =models.CharField(max_length=100,blank=False)
    Pincode = models.CharField(max_length=10,blank=False)
    contactNumber = models.IntegerField(max_length=15,blank=False)
    class Meta:
        abstract = True

    def __str__(self):
        return 'User_Id : {0} , Password {1}'.format(self.User_Id, self.Password)

class CustomerAccount(Account):
    pass
AccountType = models.CharField(max_length=10,default="Customer")

class DriverAccount(Account) :
    pass
AccountType = models.CharField(max_length=10,default="driver")

class AdminAccount(Account) :
    pass

AccountType = models.CharField(max_length=10,default="admin")
"""

class Account(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_ID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address_line1 = models.CharField(db_column='Address_Line1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address_line2 = models.CharField(db_column='Address_Line2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='Pincode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact_number = models.IntegerField(db_column='Contact_Number', blank=True, null=True)  # Field name made lowercase.
    user_type_id = models.IntegerField(db_column='User_Type_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'

class UserType(models.Model):
    user_type_id = models.IntegerField(db_column='User_Type_ID', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='User_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_type'
  

class Bin(models.Model):
    bin_id = models.IntegerField(db_column='Bin_ID', primary_key=True)  # Field name made lowercase.
    bin_type = models.CharField(db_column='Bin_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bin_weight = models.IntegerField(db_column='Bin_Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bin'


class Block(models.Model):
    block_id = models.IntegerField(db_column='Block_ID', primary_key=True)  # Field name made lowercase.
    block_name = models.CharField(db_column='Block_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    route_id = models.IntegerField(db_column='Route_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'block'

class Customer(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    block_id = models.IntegerField(db_column='Block_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

class MessageDetail(models.Model):
    message_id = models.IntegerField(db_column='Message_ID', primary_key=True)  # Field name made lowercase.
    message_description = models.CharField(db_column='Message_Description', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'message_detail'


class NotificationDetail(models.Model):
    notification_id = models.IntegerField(db_column='Notification_ID', primary_key=True)  # Field name made lowercase.
    request_id = models.IntegerField(db_column='Request_ID', blank=True, null=True)  # Field name made lowercase.
    message_id = models.IntegerField(db_column='Message_ID', blank=True, null=True)  # Field name made lowercase.
    notification_type = models.CharField(db_column='Notification_Type', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification_detail'


class RequestDetail(models.Model):
    request_id = models.IntegerField(db_column='Request_ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID', blank=True, null=True)  # Field name made lowercase.
    trip_id = models.IntegerField(db_column='Trip_ID', blank=True, null=True)  # Field name made lowercase.
    request_type = models.CharField(db_column='Request_Type', max_length=128, blank=True, null=True)  # Field name made lowercase.
    request_date = models.DateField(db_column='Request_Date', blank=True, null=True)  # Field name made lowercase.
    pickup_date = models.DateField(db_column='Pickup_Date', blank=True, null=True)  # Field name made lowercase.
    request_status = models.CharField(db_column='Request_status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bin_id = models.IntegerField(db_column='Bin_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request_detail'


class Route(models.Model):
    route_id = models.IntegerField(db_column='Route_ID', primary_key=True)  # Field name made lowercase.
    route_name = models.CharField(db_column='Route_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'route'


class Trip(models.Model):
    trip_id = models.IntegerField(db_column='Trip_ID', primary_key=True)  # Field name made lowercase.
    trip_date = models.DateField(db_column='Trip_Date', blank=True, null=True)  # Field name made lowercase.
    route_id = models.IntegerField(db_column='Route_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trip'


class Truck(models.Model):
    truck_id = models.IntegerField(db_column='Truck_ID', primary_key=True)  # Field name made lowercase.
    trip_id = models.IntegerField(db_column='Trip_ID', blank=True, null=True)  # Field name made lowercase.
    truck_capacity = models.IntegerField(db_column='Truck_Capacity', blank=True, null=True)  # Field name made lowercase.
    truck_type = models.IntegerField(db_column='Truck_Type', blank=True, null=True)  # Field name made lowercase.
    truck_weight = models.IntegerField(db_column='Truck_Weight', blank=True, null=True)  # Field name made lowercase.
    truck_status = models.CharField(db_column='Truck_Status', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'truck'


class TruckDriver(models.Model):
    truck_driver_id = models.IntegerField(db_column='Truck_Driver_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    driver_status = models.CharField(db_column='Driver_status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    service_hours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truck_driver'



