# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_panel', '0014_auto_20170801_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfomodel',
            old_name='personal_email',
            new_name='e_mail',
        ),
        migrations.RenameField(
            model_name='studentinfomodel',
            old_name='student_email',
            new_name='e_mail',
        ),
    ]
