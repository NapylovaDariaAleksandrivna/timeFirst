from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Pepople(models.Model):
    class I_te(models.TextChoices):
        IRIT="IRIT",'ИРИТ'
        INEU="INEU",'ИНЭУ'
        IFHTiM="IFHTiM",'ИФХТиМ'
        INEL="INEL",'ИНЭЛ'
        IPTM="IPTM",'ИПТМ'
        ITS="ITS",'ИТС'
        ITAEiTF="ITAEiTF",'ИЯЭиТФ'
    
    institute=models.CharField(max_length=7,choices=I_te.choices)
    username = models.CharField(max_length=150, unique=True)
    group = models.CharField(max_length=25)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=15)

    USERNAME_FIELD = 'username'


