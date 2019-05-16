from rest_framework import serializers
from xRides_api.models import Rides

class xRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Rides
        fields = ('id','user_id','vehicle_model_id','package_id','travel_type_id','from_area_id','to_area_id','from_city_id' ,'to_city_id' ,'from_date','to_date','online_booking','mobile_site_booking','booking_created','from_lat','from_long','to_lat','to_long','car_cancellation')

    def create(self, validated_data):
        """
        Create and return a new `Rides` instance, given the validated data.
        """
        return Rides.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `rides` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.vehicle_model_id = validated_data.get('vehicle_model_id', instance.vehicle_model_id)
        instance.package_id = validated_data.get('package_id', instance.package_id)
        instance.travel_type_id = validated_data.get('travel_type_id', instance.travel_type_id)
        instance.from_area_id = validated_data.get('from_area_id', instance.from_area_id)
        instance.to_area_id = validated_data.get('to_area_id', instance.to_area_id)
        instance.from_city_id = validated_data.get('from_city_id', instance.from_city_id)
        instance.to_city_id = validated_data.get('to_city_id', instance.to_city_id)
        instance.from_date = validated_data.get('from_date', instance.from_date)
        instance.to_date = validated_data.get('to_date', instance.to_date)
        instance.online_booking = validated_data.get('online_booking', instance.online_booking)
        instance.mobile_site_booking = validated_data.get('mobile_site_booking', instance.mobile_site_booking)
        instance.booking_created = validated_data.get('booking_created', instance.booking_created)
        instance.from_lat = validated_data.get('from_lat', instance.from_lat)
        instance.from_long = validated_data.get('from_long', instance.from_long)
        instance.to_lat = validated_data.get('to_lat', instance.to_lat)
        instance.to_long = validated_data.get('to_long', instance.to_long)
        instance.car_cancellation = validated_data.get('car_cancellation', instance.car_cancellation)
        instance.save()
        return instance