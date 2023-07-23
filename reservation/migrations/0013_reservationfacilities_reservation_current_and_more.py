# Generated by Django 4.1.7 on 2023-07-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0012_reservationfacilities_patient"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservationfacilities",
            name="reservation_current",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reservationfacilities",
            name="reservation_limit",
            field=models.IntegerField(default="1"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reservationfacilities",
            name="timeslot",
            field=models.CharField(
                choices=[("1", "6:00AM - 12:00NN"), ("2", "1:00PM - 6:00PM")],
                max_length=1,
                null=True,
            ),
        ),
    ]