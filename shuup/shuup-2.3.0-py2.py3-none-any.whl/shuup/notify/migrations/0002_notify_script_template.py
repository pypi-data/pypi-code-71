# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-09 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='template',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='template identifier'),
        ),
    ]
