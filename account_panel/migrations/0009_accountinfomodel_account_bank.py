# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0008_auto_20170713_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfomodel',
            name='account_bank',
            field=models.CharField(choices=[('149', 'Suadiye-HalkBank')], default='149', max_length=20, verbose_name='Account Bank'),
        ),
    ]
