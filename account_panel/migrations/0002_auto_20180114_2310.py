# Generated by Django 2.0.1 on 2018-01-14 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfomodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='periodicpaymentmodel',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='periodicpaymentmodel',
            name='person_asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account_panel.PersonAssetInfoModel'),
        ),
        migrations.AlterField(
            model_name='personassetinfomodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='personassetinfomodel',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='person_panel.StudentInfoModel'),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_panel.AccountInfoModel'),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.CompanyInfoModel'),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 14, 23, 10, 5, 103113)),
        ),
    ]
