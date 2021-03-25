from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)  
    last_name =  models.CharField(max_length=100)
    age=models.IntegerField()
    country= models.CharField(max_length=50)
    phone= models.CharField(max_length=20)
    balance = models.IntegerField()