from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    Firstname = models.CharField(null=True)
    Lastname= models.CharField(null=True)
   
    
    class Meta:
        db_table = 'user'


