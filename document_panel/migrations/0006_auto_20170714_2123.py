# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_panel', '0005_auto_20170713_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='liability_lastday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 21, 21, 23, 48, 443942), null=True, verbose_name='Liability Last day'),
        ),
    ]
