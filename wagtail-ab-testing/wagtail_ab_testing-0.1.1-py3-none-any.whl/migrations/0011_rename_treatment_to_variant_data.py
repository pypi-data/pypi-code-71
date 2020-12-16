# Generated by Django 3.1.3 on 2020-12-16 13:40

from django.db import migrations, models


def rename_treatment_to_variant_forwards(apps, schema_editor):
    AbTest = apps.get_model('wagtail_ab_testing.AbTest')
    AbTest.objects.filter(winning_version='treatment').update(winning_version='variant')

    AbTestHourlyLog = apps.get_model('wagtail_ab_testing.AbTestHourlyLog')
    AbTestHourlyLog.objects.filter(version='treatment').update(version='variant')


def rename_treatment_to_variant_backwards(apps, schema_editor):
    AbTest = apps.get_model('wagtail_ab_testing.AbTest')
    AbTest.objects.filter(winning_version='variant').update(winning_version='treatment')

    AbTestHourlyLog = apps.get_model('wagtail_ab_testing.AbTestHourlyLog')
    AbTestHourlyLog.objects.filter(version='variant').update(version='treatment')


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_ab_testing', '0010_rename_treatment_to_variant'),
    ]

    operations = [
        migrations.RunPython(rename_treatment_to_variant_forwards, rename_treatment_to_variant_backwards)
    ]
