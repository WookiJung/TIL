from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username, password, is_active, is_staff, ...etc columns
    address = models.CharField(max_length=100)
