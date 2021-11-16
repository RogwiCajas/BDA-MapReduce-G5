from django.db import models
from django.db.models import fields
from rest_framework import serializers
from TaxiApp.models import TaxisModel

class TaxisSerializer(serializers.ModelSerializer):
    class Meta: 
        model=TaxisModel
        fields=('company', 'dropoff_community_area' , 'dropoff_latitude' ,'dropoff_location' , 'dropoff_longitude', 'extras','fare', 'payment_type','pickup_community_area','pickup_latitude','pickup_location','pickup_longitude' ,'taxi_id','tips', 'tolls', 'trip_end_timestamp', 'trip_miles', 'trip_seconds', 'trip_start_timestamp', 'trip_total','unique_key' )  