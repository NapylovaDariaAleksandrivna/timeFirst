from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Pepople(AbstractUser):
    TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
    )
    username = models.CharField(max_length=150, unique=True)
    id = models.AutoField(primary_key=True)
    password= models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    flag=models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False)


