# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0003_auto_20171003_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_expired',
            field=models.DateField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.CharField(default='profile_pic/1701001', max_length=200),
        ),
    ]