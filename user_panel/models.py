# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class CompanyInfoModel(models.Model):
    company_type=[]
    company_id=models.CharField(max_length=10,primary_key=True)
    company_name=models.CharField(max_length=20,default='')
    company_vno=models.CharField(max_length=15,default='')
    company_adress=models.CharField(max_length=100,default='',null=True,blank=True)
    company_account_no=models.CharField(max_length=15,default='',null=True,blank=True)
    company_payment_detail=models.CharField(max_length=50,default='',null=True,blank=True)
    company_desc=models.CharField(max_length=100,default='',null=True,blank=True)

    class Meta:
        db_table='company_info'

    def __str__(self):
        return str(self.company_id)

    def company_type_name(self):
        return None

# class UserInfoModel(AbstractUser):
#     image_field=models.ImageField(upload_to='profile_pic/',default='',verbose_name='Profil Resmi',blank=True,null=True)
#     company_id=models.ForeignKey(CompanyInfoModel)
#

class UserCompanyModel(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    company=models.ForeignKey(CompanyInfoModel)

    class Meta:
        db_table='user_company'

    def __str__(self):
        return str(self.id)