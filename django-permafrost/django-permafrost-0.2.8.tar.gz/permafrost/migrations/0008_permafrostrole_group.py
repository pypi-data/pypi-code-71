# Generated by Django 3.0.3 on 2020-04-30 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('permafrost', '0007_remove_permafrostrole_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='permafrostrole',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Group'),
        ),
    ]
