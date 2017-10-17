# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20171014_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='created_hour',
        ),
        migrations.AddField(
            model_name='transaction',
            name='valid_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 15, 18, 48, 515861, tzinfo=utc)),
        ),
    ]