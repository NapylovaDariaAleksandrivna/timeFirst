from django.db import models
from django.contrib.auth.models import AbstractUser
from voting.models import V
# Create your models here.

class Pepople(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    id = models.AutoField(primary_key=True)
    password= models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    flag=models.ForeignKey(V, on_delete=models.CASCADE, null=True, default=None)
    REQUIRED_FIELDS = ['email']

    def getFlag(self):
        return self.flag!=None
    def setFlag(self,f):
        self.flag=f
