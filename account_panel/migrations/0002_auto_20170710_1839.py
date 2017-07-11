# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='transaction_type',
            field=models.CharField(default='1', max_length=10, verbose_name='Transaction Type: '),
        ),
        migrations.AlterModelTable(
            name='accountinfomodel',
            table='account_info',
        ),
        migrations.AlterModelTable(
            name='billinfomodel',
            table='bill_info',
        ),
        migrations.AlterModelTable(
            name='personassetinfomodel',
            table='personasset_info',
        ),
        migrations.AlterModelTable(
            name='transactioninfomodel',
            table='transaction_info',
        ),
    ]