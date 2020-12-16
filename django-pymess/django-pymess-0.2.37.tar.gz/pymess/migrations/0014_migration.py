# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-08 23:02
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import Func, F, Value


def copy_external_id_from_extra_data(apps, schema_editor):
    EmailMessage = apps.get_model('pymess', 'EmailMessage')
    EmailMessage.objects.all().update(
        external_id=Func(F('extra_sender_data'), Value('^.*"_id":"([^"]*)".*$'), function='substring')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('pymess', '0013_migration'),
    ]

    operations = [
        migrations.RunPython(copy_external_id_from_extra_data),
    ]
