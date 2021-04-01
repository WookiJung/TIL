from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
# accounts.models

class User(AbstractUser):
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed')

    
    def __str__(self):
        return f'{self.pk} : {self.username}'
    



# class image(models.Model):
#     image = models.ImageField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)