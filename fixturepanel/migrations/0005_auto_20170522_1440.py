# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixturepanel', '0004_auto_20170521_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtureinfomodel',
            name='room_no',
            field=models.CharField(choices=[('101', '101'), ('102', '102'), ('103', '103'), ('201', '201'), ('202', '202'), ('203', '203'), ('301', '301'), ('302', '302'), ('303', '303'), ('401', '401'), ('402', '402'), ('403', '403')], max_length=5),
        ),
    ]
