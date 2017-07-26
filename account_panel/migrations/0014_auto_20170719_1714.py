# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0013_auto_20170717_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinfomodel',
            name='bill_type',
            field=models.CharField(choices=[('1', 'Su'), ('2', 'Doğalgaz'), ('3', 'Elektrik'), ('4', 'Internet'), ('5', 'Telefon'), ('6', 'Vergi')], max_length=10, verbose_name='Bill Type: '),
        ),
    ]