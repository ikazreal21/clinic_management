# Generated by Django 4.1.7 on 2023-04-04 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReserveConsulation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("speciality", models.CharField(max_length=255)),
                ("doctor", models.CharField(max_length=255)),
                ("is_approve", models.BooleanField(default=False)),
                ("schedule", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Results",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient", models.CharField(max_length=255)),
                ("is_facility", models.BooleanField(default=False)),
                ("result_file", models.FileField(upload_to="")),
                ("description", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ReservationServices",
        ),
    ]
