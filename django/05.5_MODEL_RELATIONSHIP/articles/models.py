from django.db import models

# Create your models here.
class ConvenientStore(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    direct = models.BooleanField()


class Item(models.Model):
    store = models.ForeignKey(ConvenientStore, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expire_date = models.Datetimefield()  

class Category(models.Model):
    name = models.CharField(max_length=20)
