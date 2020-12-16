# Generated by Django 3.1.3 on 2020-11-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sovtimer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AaSovtimerCampaigns",
            fields=[
                (
                    "campaign_id",
                    models.PositiveBigIntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("attackers_score", models.FloatField()),
                ("constellation_id", models.PositiveBigIntegerField()),
                ("defender_id", models.PositiveBigIntegerField()),
                ("defender_score", models.FloatField()),
                ("event_type", models.CharField(max_length=12)),
                ("solar_system_id", models.PositiveBigIntegerField()),
                ("start_time", models.DateTimeField()),
                ("structure_id", models.PositiveBigIntegerField()),
            ],
            options={
                "verbose_name": "Sovereignty Campaign",
                "verbose_name_plural": "Sovereignty Campaigns",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="AaSovtimerStructures",
            fields=[
                (
                    "structure_id",
                    models.PositiveBigIntegerField(
                        db_index=True, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("alliance_id", models.PositiveBigIntegerField()),
                ("solar_system_id", models.PositiveBigIntegerField()),
                ("structure_type_id", models.PositiveBigIntegerField()),
                ("vulnerability_occupancy_level", models.FloatField(null=True)),
                ("vulnerable_end_time", models.DateTimeField(null=True)),
                ("vulnerable_start_time", models.DateTimeField(null=True)),
            ],
            options={
                "verbose_name": "Sovereignty Structure",
                "verbose_name_plural": "Sovereignty Structures",
                "default_permissions": (),
            },
        ),
    ]
