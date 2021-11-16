from django.db import models
from django.db.models import fields
from rest_framework import serializers
from TaxiApp.models import TaxisModel

class TaxisSerializar(serializers.ModelSerializer):
    class Meta: 
        model=TaxisModel
        fields-('company', 'dropoffCommunityArea' , 'dropoffLatitude' ,'dropoffLocation' , 'dropoffLongitude', 'extras','fare', 'paymentType','pickupCommunityArea','pickupLatitude','pickupLocation','pickupLongitude' ,'taxiId','tips', 'tolls', 'tripEndTimestamp', 'tripMiles', 'tripSeconds', 'tripStartTimestamp', 'tripTotal','uniqueKey' )     



    
     
   