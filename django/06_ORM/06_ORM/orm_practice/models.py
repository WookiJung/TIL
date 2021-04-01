from django.db import models
# python mange.py shell_plus --print-sql
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    balance = models.IntegerField()