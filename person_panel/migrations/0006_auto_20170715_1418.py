# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_panel', '0005_auto_20170715_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfomodel',
            name='student_tcn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='person_panel.PersonIDInfoModel', verbose_name='Öğrencinin Kimlik Numarası'),
        ),
    ]