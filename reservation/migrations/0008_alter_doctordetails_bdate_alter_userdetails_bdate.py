# Generated by Django 4.1.7 on 2023-04-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0007_reserveconsulation_date_created_messages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctordetails",
            name="bdate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="bdate",
            field=models.DateField(blank=True, null=True),
        ),
    ]
