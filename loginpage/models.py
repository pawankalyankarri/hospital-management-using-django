from django.db import models
from django.views import View
# Create your models here.

class Employees(models.Model):
    empid = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=40)
    empgender = models.CharField(max_length=10)
    empmobile = models.CharField(max_length=18)
    empusername = models.CharField(max_length=40)
    emppassword = models.CharField(max_length=18)
    
    
    