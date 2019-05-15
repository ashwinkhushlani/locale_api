# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Rides(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    vehicle_model_id = models.IntegerField(blank=True, null=True)
    package_id = models.IntegerField(blank=True, null=True)
    travel_type_id = models.IntegerField(blank=True, null=True)
    from_area_id = models.IntegerField(blank=True, null=True)
    to_area_id = models.IntegerField(blank=True, null=True)
    from_city_id = models.IntegerField(blank=True, null=True)
    to_city_id = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    online_booking = models.BooleanField(blank=True, null=True)
    mobile_site_booking = models.BooleanField(blank=True, null=True)
    booking_created = models.DateTimeField(blank=True, null=True)
    from_lat = models.FloatField(blank=True, null=True)
    from_long = models.FloatField(blank=True, null=True)
    to_lat = models.FloatField(blank=True, null=True)
    to_long = models.FloatField(blank=True, null=True)
    car_cancellation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rides'
