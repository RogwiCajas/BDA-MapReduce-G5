from rest_framework import serializers

from taxis_chicago.constants import STATUS_CHOICES


class TaxisSerializer(serializers.Serializer):
    #id = serializers.CharField(max_length=200, read_only=True)
    
    company = serializers.CharField(max_length=300)
    dropoffCommunityArea = serializers.IntegerField()
    dropoffLatitude = serializers.FloatField()
    dropoffLocation = serializers.CharField(max_length=400)
    dropoffLongitude = serializers.FloatField()
    extras = serializers.IntegerField()
    fare = serializers.FloatField()
    paymentType = serializers.CharField(max_length=300)
    pickupCommunityArea = serializers.IntegerField()
    pickupLatitude = serializers.FloatField()
    pickupLocation = serializers.CharField(max_length=400)
    pickupLongitude = serializers.FloatField()
    taxiId = serializers.CharField(max_length=500)
    tips = serializers.FloatField()
    tolls = serializers.CharField(max_length=100)
    tripEndTimestamp = serializers.DateTimeField()
    tripMiles = serializers.FloatField()
    tripSeconds = serializers.IntegerField()
    tripStartTimestamp = serializers.DateTimeField()
    tripTotal = serializers.FloatField()
    uniqueKey = serializers.CharField(max_length=200, read_only=True)

