# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-23 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20170403_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='weight_unit',
            field=models.CharField(choices=[('kg', 'Metric (kilogram)'), ('lb', 'Imperial (pound)')], default='lb', max_length=2, verbose_name='Weight unit'),
        ),
    ]
