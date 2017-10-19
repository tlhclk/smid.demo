# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_panel', '0008_auto_20171007_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfomodel',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='accountinfomodel',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='accountinfomodel',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='accountinfomodel',
            name='no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='accountinfomodel',
            name='type',
            field=models.CharField(choices=[('1', 'Vadesiz Banka Hesabı'), ('2', 'Vadeli Banka Hesabı'), ('3', 'Nakit'), ('4', 'Senet'), ('5', 'Çek'), ('6', 'Kredi Kartı Hesabı')], max_length=40),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='period',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='billinfomodel',
            name='type',
            field=models.CharField(choices=[('1', 'Su'), ('2', 'Doğalgaz'), ('3', 'Elektrik'), ('4', 'Internet'), ('5', 'Telefon'), ('6', 'Vergi')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='account_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_panel.AccountInfoModel'),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='transactioninfomodel',
            name='type',
            field=models.CharField(choices=[('', ''), ('1', 'Para Yatırma'), ('2', 'Para Çekme'), ('3', 'Havale'), ('4', 'EFT'), ('5', 'Kredi Kartı Borcu Ödeme'), ('6', 'Fatura Ödeme'), ('7', 'Öğrenci Ödemesi')], default='1', max_length=10),
        ),
    ]