# Generated by Django 2.2.15 on 2020-11-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psu_base', '0018_auto_20201105_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='stacktrace',
            field=models.TextField(blank=True, help_text='StackTrace', null=True),
        ),
    ]
