# Generated by Django 4.1.7 on 2023-04-09 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0013_remove_doctordetails_speciality_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
