from django.db import models
import datetime
# Create your models here.
class Workers(models.Model):
    w_id = models.PositiveIntegerField(null=True)
    dtstamp = models.DateTimeField(datetime.datetime, blank=True, null=True)
    w_name = models.CharField(max_length=20, blank=True, null=True)
    w_email = models.CharField(max_length=20, blank=True, null=True)
    w_phone = models.CharField(max_length=20, blank=True, null=True)
    w_remarks = models.CharField(max_length=20, blank=True, null=True)
    test = models.TextField( blank=True, null=True)
    # def __str__(self):   