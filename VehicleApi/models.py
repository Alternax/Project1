#Imports
import datetime
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    v_id = models.PositiveIntegerField(null=True)
    dtstamp = models.DateTimeField(datetime.datetime, blank=True, null=True)
    v_regnNo = models.CharField(max_length=20, blank=True, null=True)
    v_model = models.CharField(max_length=20, blank=True, null=True)
    v_make = models.CharField(max_length=20, blank=True, null=True)
    v_remarks = models.CharField(max_length=20, blank=True, null=True)
    test = models.TextField( blank=True, null=True)

   
