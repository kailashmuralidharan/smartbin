from django.db import models

# Create your models here.
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

  

