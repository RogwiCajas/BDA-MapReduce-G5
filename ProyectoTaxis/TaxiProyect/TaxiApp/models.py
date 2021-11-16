from django.db import models

# Create your models here.
class TaxisModel(models.Model):
    company = models.CharField(max_length=300, null=True)
    dropoffCommunityArea = models.IntegerField(null=True)
    dropoffLatitude = models.FloatField(null=True)
    dropoffLocation = models.CharField(max_length=400, null=True)
    dropoffLongitude = models.FloatField(null=True)
    extras = models.FloatField(null=True)
    fare = models.FloatField(null=True)
    paymentType = models.CharField(max_length=300, null=True)
    pickupCommunityArea = models.IntegerField(null=True)
    pickupLatitude = models.FloatField(null=True)
    pickupLocation = models.CharField(max_length=400, null=True)
    pickupLongitude = models.FloatField(null=True)
    taxiId = models.CharField(max_length=500, null=False)
    tips = models.FloatField(null=True)
    tolls = models.FloatField(null=True)
    tripEndTimestamp = models.CharField(max_length=100, null=True)
    tripMiles = models.FloatField(null=True)
    tripSeconds = models.IntegerField(null=True)
    tripStartTimestamp = models.CharField(max_length=100, null=True)
    tripTotal = models.FloatField(null=True)
    uniqueKey = models.CharField(max_length=500,null=False)

