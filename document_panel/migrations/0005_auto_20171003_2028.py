# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document_panel', '0004_auto_20171003_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentinfomodel',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='documentinfomodel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_panel.StudentInfoModel', verbose_name='Person id: '),
        ),
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='liabilityinfomodel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_panel.StudentInfoModel', verbose_name='Person Id: '),
        ),
    ]