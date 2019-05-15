from rest_framework import serializers
from xRides_api.serializers import Rides

class xRidesSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    vehicle_model_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    package_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    travel_type_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    from_area_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    to_area_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    from_city_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    to_city_id = serializers.IntegerField(allow_blank=True, allow_null=True)
    from_date = serializers.DateTimeField(allow_blank=True, allow_null=True)
    to_date = serializers.DateTimeField(allow_blank=True, allow_null=True)
    online_booking = serializers.BooleanField(allow_blank=True, allow_null=True)
    mobile_site_booking = serializers.BooleanField(allow_blank=True, allow_null=True)
    booking_created = serializers.DateTimeField(allow_blank=True, allow_null=True)
    from_lat = serializers.FloatField(allow_blank=True, allow_null=True)
    from_long = serializers.FloatField(allow_blank=True, allow_null=True)
    to_lat = serializers.FloatField(allow_blank=True, allow_null=True)
    to_long = serializers.FloatField(allow_blank=True, allow_null=True)
    car_cancellation 

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
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