# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person_panel', '0003_personalinfomodel_salary'),
        ('user_panel', '0005_auto_20171101_1307'),
        ('operation_panel', '0002_auto_20171030_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('company_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_panel.PersonalInfoModel')),
            ],
            options={
                'db_table': 'vacation_info',
            },
        ),
        migrations.AlterField(
            model_name='studentleavemodel',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentleavemodel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person_panel.StudentInfoModel'),
        ),
        migrations.AlterField(
            model_name='studentleavemodel',
            name='reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentleavemodel',
            name='start',
            field=models.DateField(),
        ),
    ]