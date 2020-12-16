# Generated by Django 2.2.11 on 2020-03-31 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0001_initial'),
        ('ansible', '0016_add_extension'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('policy', models.CharField(choices=[('blacklist', 'blacklist'), ('whitelist', 'whitelist')], default='blacklist', max_length=64)),
                ('groups', models.ManyToManyField(related_name='synclists', to='galaxy.Group')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansible.AnsibleRepository')),
                ('collections', models.ManyToManyField(to='ansible.Collection')),
                ('namespaces', models.ManyToManyField(to='galaxy.Namespace')),
                ('users', models.ManyToManyField(related_name='synclists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
