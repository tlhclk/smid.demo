# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 14:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_panel', '0010_auto_20170715_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='liability_lastday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 23, 17, 29, 20, 367033), null=True, verbose_name='Liability Last day'),
        ),
    ]