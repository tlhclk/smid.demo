# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.db import models
# import datetime
#
# class TransactionInfoModel(models.Model):
#     debit_credit_list=[('1','debitin'),('2','creditout')]
#     transaction_type_list=[]
#     transaction_no=models.CharField(max_length=10,primary_key=True,verbose_name='Transaction No: ')
#     account_no=models.ForeignKey(AccountInfoModel,verbose_name='Account No:')
#     transaction_type=models.CharField(max_length=10,choices=transaction_type_list,verbose_name='Transaction Type: ')
#     transaction_amount=models.CharField(max_length=10,verbose_name='Transaction Amount: ')
#     transaction_debit_credit=models.CharField(max_length=10,choices=debit_credit_list,verbose_name='Transaction is Debit or Credit: ')
#     transaction_time=models.DateTimeField(default=datetime.datetime.now)
#     transaction_desc=models.CharField(max_length=50,verbose_name='Transaction Description: ')
#
# class PersonAssetInfoModel(models.Model):
#     asset_id=models.CharField(max_length=10,primary_key=True,verbose_name='Individual Asset ID: ')
#     person_id=models.CharField(max_length=10,verbose_name='Person ID: ')
#     asset_amount=models.CharField(max_length=10,verbose_name='Asset Amount: ')
#     asset_debt=models.CharField(max_length=10,verbose_name='Asset Debt: ')
#     asset_desc=models.CharField(max_length=50,verbose_name='Asset Description: ')
#
# class AccountInfoModel(models.Model):
#     account_type_list=[]
#     account_no=models.CharField(max_length=10,verbose_name='Account No: ',primary_key=True)
#     account_name=models.CharField(max_length=10,verbose_name='Account Name: ')
#     account_type=models.CharField(max_length=10,verbose_name='Account Type: ',choices=account_type_list)
#     account_amount=models.CharField(max_length=10,verbose_name='Account Amount: ',blank=True)
#     account_desc=models.CharField(max_length=10,verbose_name='Account Description: ',blank=True)
#
# class BillInfoModel(models.Model):
#     bill_type_list=[]
#     bill_no=models.CharField(max_length=10,verbose_name='Bill No: ',primary_key=True)
#     bill_type=models.CharField(max_length=10,verbose_name='Bill Type: ',choices=bill_type_list)
#     bill_code=models.CharField(max_length=10,verbose_name='Bill Code: ')
#     bill_desc=models.CharField(max_length=100,verbose_name='Bill Description: ')
#     bill_address=models.CharField(max_length=100,verbose_name='Bill Adress: ')
#     bill_period=models.CharField(max_length=10,verbose_name='Bill Period: ')
#     bill_last_date=models.DateField(default=datetime.date.today)