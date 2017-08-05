# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_panel', '0008_auto_20170723_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentinfomodel',
            name='id',
            field=models.CharField(default='1704001', max_length=8, primary_key=True, serialize=False, verbose_name='Veli No'),
        ),
        migrations.AlterField(
            model_name='personalinfomodel',
            name='id',
            field=models.CharField(default='', max_length=7, primary_key=True, serialize=False, verbose_name='Personel No'),
        ),
        migrations.AlterField(
            model_name='personidinfomodel',
            name='s_lastname',
            field=models.CharField(default='', max_length=50, verbose_name='Soyisim'),
        ),
        migrations.AlterField(
            model_name='personidinfomodel',
            name='s_name',
            field=models.CharField(default='', max_length=50, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='personidinfomodel',
            name='s_tcn',
            field=models.CharField(default='', max_length=11, primary_key=True, serialize=False, verbose_name='TC No'),
        ),
    ]
