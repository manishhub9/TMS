# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_auto_20171015_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cash_paid',
            field=models.BooleanField(default=False),
        ),
    ]
