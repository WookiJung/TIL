from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
