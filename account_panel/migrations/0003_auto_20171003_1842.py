# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0002_auto_20171003_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfomodel',
            name='company_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='company_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='personassetinfomodel',
            name='company_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='company_id',
            field=models.CharField(max_length=10),
        ),
    ]