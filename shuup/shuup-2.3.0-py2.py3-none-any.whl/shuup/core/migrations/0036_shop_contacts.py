# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-02 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0035_remove_shop_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='shops',
            field=models.ManyToManyField(blank=True, to='shuup.Shop'),
        ),
    ]
