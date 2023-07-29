# Generated by Django 4.1.7 on 2023-07-09 07:06

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0007_alter_results_result_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
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
                (
                    "result_file",
                    models.FileField(
                        storage=django.core.files.storage.FileSystemStorage(
                            location="/pdf_file"
                        ),
                        upload_to="",
                    ),
                ),
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
    ]
