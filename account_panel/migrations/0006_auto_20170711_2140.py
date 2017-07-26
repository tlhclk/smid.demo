# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0005_auto_20170711_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinfomodel',
            name='bill_address',
            field=models.CharField(default='-', max_length=200, verbose_name='Bill Adress: '),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='bill_type',
            field=models.CharField(choices=[('1', '\u0130SK\u0130')], max_length=10, verbose_name='Bill Type: '),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='transaction_type',
            field=models.CharField(choices=[('1', 'Para Yat\u0131rma'), ('2', 'Para \xc7ekme'), ('3', 'Havale'), ('4', 'EFT'), ('5', 'Kredi Kart\u0131 Borcu \xd6deme'), ('6', 'Fatura \xd6deme'), ('7', 'Tahsilat')], default='1', max_length=10, verbose_name='Transaction Type: '),
        ),
    ]