# Generated by Django 4.1.7 on 2023-04-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0009_alter_doctordetails_bdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctordetails",
            name="bdate",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="bdate",
            field=models.DateField(),
        ),
    ]
