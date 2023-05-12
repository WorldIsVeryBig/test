# Generated by Django 4.2.1 on 2023-05-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Registrations",
            "0003_rename_app_mobility_services_app_mobility_services_models",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="subscription_models",
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
                (
                    "subscriptionId",
                    models.CharField(default="unverified", max_length=64),
                ),
            ],
        ),
    ]