from rest_framework import serializers

from taxis_chicago.constants import STATUS_CHOICES


class TaxisSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200, read_only=True)
    company = serializers.CharField(max_length=300,allow_blank=True, allow_null=True)
    dropoffCommunityArea = serializers.IntegerField(allow_null=True)
    dropoffLatitude = serializers.FloatField(allow_null=True)
    dropoffLocation = serializers.CharField(max_length=400,allow_blank=True, allow_null=True)
    dropoffLongitude = serializers.FloatField(allow_null=True)
    extras = serializers.IntegerField(allow_null=True)
    fare = serializers.FloatField(allow_null=True)
    paymentType = serializers.CharField(max_length=300,allow_blank=True, allow_null=True)
    pickupCommunityArea = serializers.IntegerField(allow_null=True)
    pickupLatitude = serializers.FloatField(allow_null=True)
    pickupLocation = serializers.CharField(max_length=400,allow_blank=True, allow_null=True)
    pickupLongitude = serializers.FloatField(allow_null=True)
    taxiId = serializers.CharField(max_length=500,allow_blank=True, allow_null=True)
    tips = serializers.FloatField(allow_null=True)
    tolls = serializers.CharField(max_length=100)
    tripEndTimestamp = serializers.DateTimeField(allow_null=True)
    tripMiles = serializers.FloatField(allow_null=True)
    tripSeconds = serializers.IntegerField(allow_null=True)
    tripStartTimestamp = serializers.DateTimeField(allow_null=True)
    tripTotal = serializers.FloatField(allow_null=True)
    uniqueKey = serializers.CharField(max_length=200, read_only=True)

