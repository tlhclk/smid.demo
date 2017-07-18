# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel


class PersonAssetInfoModel(models.Model):
    asset_type_list=[('1','Nakit'),('2','Kredi Kartı'),('3','Para Transferi'),('4','Online Ödeme')]
    asset_id=models.CharField(max_length=10,primary_key=True,verbose_name='Individual Asset ID: ')
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person id')
    #person_id=models.CharField(max_length=10,verbose_name='Person ID: ')
    asset_amount=models.CharField(max_length=10,verbose_name='Asset Amount: ')
    asset_debt=models.CharField(max_length=10,verbose_name='Asset Debt: ')
    asset_desc=models.CharField(max_length=50,verbose_name='Asset Description: ')
    #asset_period=models.CharField(max_length=10,verbose_name='Asset period, payment time',blank=True)
    asset_type=models.CharField(max_length=10,verbose_name='Asset Type',blank=True,choices=asset_type_list)

    class Meta:
        db_table='personasset_info'

    def __str__(self):
        return self.asset_id

class AccountInfoModel(models.Model):
    account_type_list=[('1','Vadesiz Banka Hesabı'),('2','Vadeli Banka Hesabı'),('3','Nakit'),('4','Senet'),('5','Çek'),('6','Kredi Kartı Hesabı')]
    bank_code=[('149','Suadiye-HalkBank')]
    account_no=models.CharField(max_length=10,verbose_name='Account No: ',primary_key=True)
    account_name=models.CharField(max_length=20,verbose_name='Account Name: ')
    account_type=models.CharField(max_length=40,verbose_name='Account Type: ',choices=account_type_list)
    account_amount=models.CharField(max_length=10,verbose_name='Account Amount: ',blank=True)
    account_desc=models.CharField(max_length=100,verbose_name='Account Description: ',blank=True)
    account_bank=models.CharField(max_length=20, verbose_name='Account Bank', choices=bank_code,default='149')

    class Meta:
        db_table='account_info'

    def __str__(self):
        return self.account_no

    def account_type_name(self):
        return self.account_type_list[int(self.account_type)-1][1]

    def bank_code_name(self):
        return dict(self.bank_code)[int(self.account_bank)]

class BillInfoModel(models.Model):
    bill_type_list=[('1','Su'),('2','Doğalgaz'),('3','Elektrik'),('4','Internet'),('5','Telefon'),('1','Vergi'),('1','İSKİ'),('1','İSKİ')]
    #bill_no=models.CharField(max_length=10,verbose_name='Bill No: ',primary_key=True)
    bill_type=models.CharField(max_length=10,verbose_name='Bill Type: ',choices=bill_type_list)
    bill_code=models.CharField(max_length=10,verbose_name='Bill Code: ')
    bill_amount=models.CharField(max_length=10,verbose_name='Bill Amount: ')
    bill_desc=models.CharField(max_length=100,verbose_name='Bill Description: ',default='-')
    bill_address=models.CharField(max_length=200,verbose_name='Bill Adress: ',default='-')
    bill_period=models.CharField(max_length=10,verbose_name='Bill Period: ',default='-')
    bill_lastday=models.DateField(default=datetime.date.today)

    class Meta:
        db_table='bill_info'

    def bill_type_name(self):
        return self.bill_type_list[int(self.bill_type)-1][1]

class TransactionInfoModel(models.Model):
    transaction_type_list = [('1','Para Yatırma'),('2','Para Çekme'),('3','Havale'),('4','EFT'),('5','Kredi Kartı Borcu Ödeme'),('6','Fatura Ödeme'),('7','Tahsilat'),('8','Öğrenci Ödemesi')]
    #transaction_no = models.CharField(max_length=10, primary_key=True, verbose_name='Transaction No: ')
    account_no=models.ForeignKey(AccountInfoModel,verbose_name='Hesap Numarası')
    #account_no = models.CharField(max_length=10, blank=True, null=True)
    transaction_type = models.CharField(max_length=10, choices=transaction_type_list,verbose_name='İşlem Türü', default='1')
    transaction_amount = models.CharField(max_length=10, verbose_name='İşlem Miktarı')
    transaction_time = models.DateTimeField(default=datetime.datetime.now,verbose_name='İşlem Zamanı')
    transaction_desc = models.CharField(max_length=50, verbose_name='İşlem Açıklaması', blank=True,help_text='Öğrenci No:1701001 /Fatura No: 1713001')

    class Meta:
        db_table = 'transaction_info'

    def __str__(self):
        return self.id

    def transaction_type_name(self):
        return self.transaction_type_list[int(self.transaction_type) - 1][1]


    def account_name(self):
        return self.account_no.account_name