# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 12:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_panel', '0015_auto_20170720_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='liability_lastday',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 7, 28, 15, 0, 47, 302555), null=True, verbose_name='Liability Last day'),
        ),
    ]
