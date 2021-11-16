from django.db import models

# Create your models here.
class TaxisModel(models.Model):
    company = models.CharField(max_length=300, null=True)
    dropoff_community_area = models.IntegerField(null=True)
    dropoff_latitude = models.FloatField(null=True)
    dropoff_location = models.CharField(max_length=400, null=True)
    dropoff_longitude = models.FloatField(null=True)
    extras = models.FloatField(null=True)
    fare = models.FloatField(null=True)
    payment_type = models.CharField(max_length=300, null=True)
    pickup_community_area = models.IntegerField(null=True)
    pickup_latitude = models.FloatField(null=True)
    pickup_location = models.CharField(max_length=400, null=True)
    pickup_longitude = models.FloatField(null=True)
    taxi_id = models.CharField(max_length=500, null=False)
    tips = models.FloatField(null=True)
    tolls = models.FloatField(null=True)
    trip_end_timestamp = models.CharField(max_length=100, null=True)
    trip_miles = models.FloatField(null=True)
    trip_seconds = models.IntegerField(null=True)
    trip_start_timestamp = models.CharField(max_length=100, null=True)
    trip_total = models.FloatField(null=True)
    unique_key = models.CharField(max_length=500,null=False, primary_key=True)

