# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_panel', '0012_auto_20170716_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='liability_lastday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 24, 10, 32, 57, 908346), null=True, verbose_name='Liability Last day'),
        ),
    ]