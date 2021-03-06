# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-22 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sync_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(null=True)),
                ('address', models.CharField(max_length=64, null=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='system_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config_sync_type', models.IntegerField(default=0)),
                ('config_sync_access_key', models.CharField(max_length=64, null=True)),
                ('config_sync_master_url', models.CharField(max_length=64, null=True)),
                ('config_sync_interval', models.IntegerField(default=60)),
                ('config_sync_scope', models.IntegerField(null=True)),
            ],
        ),
    ]
