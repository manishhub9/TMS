# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_auto_20170928_0715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['print_name']},
        ),
        migrations.AlterModelTable(
            name='unit',
            table='unit',
        ),
    ]
