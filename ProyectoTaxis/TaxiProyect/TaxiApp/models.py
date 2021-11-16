from django.db import models

# Create your models here.
class TaxisModel(models.Model):
    company = models.CharField(max_length=300,blank=True, null=True)
    dropoffCommunityArea = models.IntegerField(null=True)
    dropoffLatitude = models.FloatField(null=True)
    dropoffLocation = models.CharField(max_length=400,blank=True, null=True)
    dropoffLongitude = models.FloatField(null=True)
    extras = models.IntegerField(null=True)
    fare = models.FloatField(null=True)
    paymentType = models.CharField(max_length=300,blank=True, null=True)
    pickupCommunityArea = models.IntegerField(null=True)
    pickupLatitude = models.FloatField(null=True)
    pickupLocation = models.CharField(max_length=400,blank=True, null=True)
    pickupLongitude = models.FloatField(null=True)
    taxiId = models.CharField(max_length=500,blank=True, null=True)
    tips = models.FloatField(null=True)
    tolls = models.CharField(max_length=100, null=True,blank=True)
    tripEndTimestamp = models.DateTimeField(null=True)
    tripMiles = models.FloatField(null=True)
    tripSeconds = models.IntegerField(null=True)
    tripStartTimestamp = models.DateTimeField(null=True)
    tripTotal = models.FloatField(null=True)
    uniqueKey = models.CharField(max_length=200,null=True)

