from django.db import models

# Create your models here.
class ConvenientStore(models.Model):
    name = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    direct = models.BooleanField()



class Item(models.Model):
    store = models.ManyToManyField(ConvenientStore, related_name='stores')
    stock = models.ManyToManyField(ConvenientStore, related_name='stocks')
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expire_date = models.Datetimefield()  

class Category(models.Model):
    name = models.CharField(max_length=20)
    for_adult = models.BooleanField()
    need_other_items = models.CharField(max_length = 100)