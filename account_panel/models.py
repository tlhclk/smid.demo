# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from person_panel.models import StudentInfoModel
from user_panel.models import CompanyInfoModel

def get_time():
    return datetime.datetime.now()

def get_date():
    return datetime.date.today()


class PersonAssetInfoModel(models.Model):
    asset_type_list=(('1','Nakit'),('2','Kredi Kartı'),('3','Para Transferi'),('4','Online Ödeme'))
    person=models.OneToOneField(StudentInfoModel,on_delete=models.CASCADE)
    debt=models.CharField(max_length=6,default='0.0')
    desc=models.CharField(max_length=50,null=True, blank=True)
    period=models.CharField(max_length=2,null=True, blank=True)
    type=models.CharField(max_length=10,choices=asset_type_list)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table='personasset_info'

    def __str__(self):
        return str(self.person)

    def type_name(self):
        return dict(self.asset_type_list)[self.type]

class AccountInfoModel(models.Model):
    account_type_list=(('1','Vadesiz Banka Hesabı'),('2','Vadeli Banka Hesabı'),('3','Nakit'),('4','Senet'),('5','Çek'),('6','Kredi Kartı Hesabı'))
    bank_code_list=(('149','HalkBank'),('150','Vakıfbank'),('151','Yapı Kredi'),('152','Ziraat'),('153','İş bankası'),('154','Akbank'))# TODO: bankalar listelenicek

    no=models.CharField(max_length=10,default='0')
    name=models.CharField(max_length=20,default='No name')
    type=models.CharField(max_length=40,choices=account_type_list)
    amount=models.CharField(max_length=10,null=True, blank=True)
    desc=models.CharField(max_length=100,null=True, blank=True)
    bank_code=models.CharField(max_length=5,choices=bank_code_list,null=True, blank=True)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table='account_info'

    def __str__(self):
        return (self.no+' - '+self.name)

    def type_name(self):
        return self.account_type_list[int(self.type)-1][1]

    def bank_code_name(self):
        return dict(self.bank_code_list)[self.bank_code]

class BillInfoModel(models.Model):
    bill_type_list=(('1','Su'),('2','Doğalgaz'),('3','Elektrik'),('4','Internet'),('5','Telefon'),('6','Vergi'))
    type=models.CharField(max_length=10,choices=bill_type_list,null=True, blank=True)
    code=models.CharField(max_length=10,default='0')
    amount=models.CharField(max_length=10,default='0')
    desc=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=200,null=True, blank=True)
    payed=models.NullBooleanField()
    last_day=models.DateField(default=get_date,max_length=10)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table='bill_info'

    def __str__(self):
        return (self.type_name()+' - '+self.code)

    def type_name(self):
        return self.bill_type_list[int(self.type)-1][1]

class TransactionInfoModel(models.Model):
    transaction_type_list = (('1','Para Yatırma'),('2','Para Çekme'),('3','Havale'),('4','EFT'),('5','Kredi Kartı Borcu Ödeme'),('6','Fatura Ödeme'),('7','Öğrenci Ödemesi'),('8','Maaş'))
    account=models.ForeignKey(AccountInfoModel,on_delete=models.CASCADE,null=True, blank=True)
    type = models.CharField(max_length=10, choices=transaction_type_list,null=True, blank=True)
    amount = models.CharField(max_length=10,null=True, blank=True)
    time = models.DateTimeField(default=get_time())
    desc = models.CharField(max_length=100,null=True,blank=True)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        db_table = 'transaction_info'

    def __str__(self):
        return str(self.account_name())+' - ' +str(self.type_name())

    def type_name(self):
        return self.transaction_type_list[int(self.type) - 1][1]

    def account_name(self):
        return self.account.name

class PeriodicPaymentModel(models.Model):
    person_asset=models.OneToOneField(PersonAssetInfoModel,on_delete=models.CASCADE)
    deposito=models.CharField(max_length=6,null=True,blank=True)
    month1=models.CharField(max_length=6,null=True,blank=True)
    month2=models.CharField(max_length=6,null=True,blank=True)
    month3=models.CharField(max_length=6,null=True,blank=True)
    month4=models.CharField(max_length=6,null=True,blank=True)
    month5=models.CharField(max_length=6,null=True,blank=True)
    month6=models.CharField(max_length=6,null=True,blank=True)
    month7=models.CharField(max_length=6,null=True,blank=True)
    month8=models.CharField(max_length=6,null=True,blank=True)
    month9=models.CharField(max_length=6,null=True,blank=True)
    month10=models.CharField(max_length=6,null=True,blank=True)
    month11=models.CharField(max_length=6,null=True,blank=True)
    month12=models.CharField(max_length=6,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True,blank=True)
    company=models.ForeignKey(CompanyInfoModel,default='',on_delete=models.CASCADE)

    class Meta:
        db_table='periodic_payment'

    def __str__(self):
        return self.person_asset

    def paid(self):
        paid=0.0
        for key,item in self.month_list():
            if item:
                paid+=float(item)
        return str(paid)

    def rest(self):
        return int(float(self.person_asset.debt)-float(self.paid()))

    def month_list(self):
        return [('9',self.month1),('10',self.month2),('11',self.month3),('12',self.month4),('1',self.month5),('2',self.month6),('3',self.month7),('4',self.month8),('5',self.month9),('6',self.month10),('7',self.month11),('8',self.month12)]

    def is_late(self):
        start_day=self.person_asset.person.start_day
        paid=float(self.paid())
        should=float(start_day.month-get_date().month)*(float(self.person_asset.debt)/float(self.person_asset.period))
        if paid<should:
            return True
        else:
            return False

