# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 21:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_panel', '0010_auto_20170711_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='liability_lastday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 20, 0, 50, 41, 886000), null=True, verbose_name=b'Liability Last day'),
        ),
    ]