# Generated by Django 2.2 on 2019-05-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xRides_api', '0002_delete_rides'),
    ]

    operations = [
        migrations.CreateModel(
            name='rides',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(null=True)),
                ('vehicle_model_id', models.IntegerField(null=True)),
                ('package_id', models.IntegerField(null=True)),
                ('travel_type_id', models.IntegerField(null=True)),
                ('from_area_id', models.IntegerField(null=True)),
                ('to_area_id', models.IntegerField(null=True)),
                ('from_city_id', models.IntegerField(null=True)),
                ('to_city_id', models.IntegerField(null=True)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('online_booking', models.BooleanField(null=True)),
                ('mobile_site_booking', models.BooleanField(null=True)),
                ('booking_created', models.DateTimeField(null=True)),
                ('from_lat', models.FloatField(null=True)),
                ('from_long', models.FloatField(null=True)),
                ('to_lat', models.FloatField(null=True)),
                ('to_long', models.FloatField(null=True)),
                ('Car_Cancellation', models.BooleanField(null=True)),
            ],
        ),
    ]
