# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel


class PersonAssetInfoModel(models.Model):
    asset_id=models.CharField(max_length=10,primary_key=True,verbose_name='Individual Asset ID: ')
    person_id=models.ForeignKey(StudentInfoModel,verbose_name='Person id')
    #person_id=models.CharField(max_length=10,verbose_name='Person ID: ')
    asset_amount=models.CharField(max_length=10,verbose_name='Asset Amount: ')
    asset_debt=models.CharField(max_length=10,verbose_name='Asset Debt: ')
    asset_desc=models.CharField(max_length=50,verbose_name='Asset Description: ')

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

    class Meta:
        db_table='account_info'

    def __str__(self):
        return self.account_no

    def account_type_name(self):
        return self.account_type_list[int(self.account_type)-1][1]

class BillInfoModel(models.Model):
    bill_type_list=[]
    bill_no=models.CharField(max_length=10,verbose_name='Bill No: ',primary_key=True)
    bill_type=models.CharField(max_length=10,verbose_name='Bill Type: ',choices=bill_type_list)
    bill_code=models.CharField(max_length=10,verbose_name='Bill Code: ')
    bill_desc=models.CharField(max_length=100,verbose_name='Bill Description: ',default='-')
    bill_address=models.CharField(max_length=100,verbose_name='Bill Adress: ',default='-')
    bill_period=models.CharField(max_length=10,verbose_name='Bill Period: ',default='-')
    bill_last_date=models.DateField(default=datetime.date.today)

    class Meta:
        db_table='bill_info'

    def __str__(self):
        return self.bill_no

    def bill_type_name(self):
        return self.bill_type_list[int(self.bill_type)-1][1]

class TransactionInfoModel(models.Model):
    debit_credit_list = [('1', 'debitin'), ('2', 'creditout')]
    transaction_type_list = []
    transaction_no = models.CharField(max_length=10, primary_key=True, verbose_name='Transaction No: ')
    account_no=models.ForeignKey(AccountInfoModel,verbose_name='Account No:')
    #account_no = models.CharField(max_length=10, blank=True, null=True)
    transaction_type = models.CharField(max_length=10, choices=transaction_type_list,verbose_name='Transaction Type: ', default='1')
    transaction_amount = models.CharField(max_length=10, verbose_name='Transaction Amount: ')
    transaction_debit_credit = models.CharField(max_length=10, choices=debit_credit_list,verbose_name='Transaction is Debit or Credit: ', default='1')
    transaction_time = models.DateTimeField(default=datetime.datetime.now)
    transaction_desc = models.CharField(max_length=50, verbose_name='Transaction Description: ', blank=True)

    class Meta:
        db_table = 'transaction_info'

    def __str__(self):
        return self.transaction_no

    def transaction_type_name(self):
        return self.transaction_type_list[int(self.transaction_type) - 1][1]

    def transation_debit_credit_name(self):
        return self.debit_credit_list[int(self.transaction_debit_credit) - 1][1]

    def account_name(self):
        return self.account_no.account_name