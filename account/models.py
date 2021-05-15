from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone 


# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_sp = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone_number = models.CharField(max_length=10)
    alt_phone_number = models.CharField(max_length=10, null=True, blank=True)
    date_create=models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.user.username

    

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    admin_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    alt_phone_no = models.CharField(max_length=10)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    pin_no = models.CharField(max_length=20)
    Area_name = models.CharField(max_length=200)
    land_mark = models.CharField(max_length=200)
    building_name = models.CharField(max_length=200)
    flate_number = models.CharField(max_length=100)
    customer = models.ManyToManyField(Customer)
    time = models.TimeField('delivery time from',null=True)
    to = models.TimeField('delivery time to',null=True)
    def __str__(self):
        return self.user.username

    

class Menu(models.Model):
    sp = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    price = models.CharField(max_length=20)
    category = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.item_name

class Order(models.Model):
    sp = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    date_of_order = models.DateTimeField(auto_now_add=True,null=True)
    no_of_orders = models.CharField(max_length=100,null=True)
    last_date = models.DateTimeField(null=True)
    duration = models.CharField(max_length=100,null=True)
    total_amount=models.FloatField(null=True)
    def __str__(self):
        return f'{self.customer.user.username} + " " +{self.date_of_order}'

class Address(models.Model):
    placeanorder = models.ForeignKey(Order,on_delete=models.CASCADE)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    pin_no = models.CharField(max_length=20)
    Area_name = models.CharField(max_length=200)
    land_mark = models.CharField(max_length=200)
    building_name = models.CharField(max_length=200)
    flate_number = models.CharField(max_length=100)
    date_create =  models.DateTimeField(auto_now_add=True)

class CustomerMenuItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=500)
    price = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    date_create =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


