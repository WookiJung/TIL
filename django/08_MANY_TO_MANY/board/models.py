from django.db import models
from django.contrib.auth.models import AbstractUser
from faker import Faker

class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(name = f.name(), address=f.address())

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like_users = models.ManyToManyField(Person, related_name='likes')
    dislike_users = models.ManyToManyField(Person, related_name = 'dislikes')

    def __str__(self):
        return f'{self.pk} : {self.title}'
    
    @classmethod
    def dummy(cls, n):
        f = Faker()
        for _ in range(n):
            cls.objects.create(title = f.address(), content='hello')
