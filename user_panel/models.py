# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.auth import get_user_model


def get_time():
    return datetime.datetime.now()
def get_date():
    return datetime.date.today()

class ChainCompanyInfoModel(models.Model):
    name=models.CharField(max_length=100,default='İsimsiz')
    person=models.CharField(max_length=100,default='Ad-Soyad')
    phone = PhoneNumberField(max_length=13,default='+905553332211')
    email =models.EmailField(unique=True,default='idle@dormoni.com')

    class Meta:
        db_table='chain_company'

    def __str__(self):
        return self.name


class CompanyInfoModel(models.Model):
    company_type=()
    name=models.CharField(max_length=20,default='İsimsiz')
    vno=models.CharField(max_length=15,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    account=models.CharField(max_length=15,null=True,blank=True)
    payment_detail=models.CharField(max_length=50,null=True,blank=True)
    chain_company=models.ForeignKey(ChainCompanyInfoModel,on_delete=models.CASCADE,null=True,blank=True)
    desc=models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table='company_info'

    def __str__(self):
        return str(self.name)

    def company_type_name(self):
        return None


## Customizing User Model
class MyUserManager(BaseUserManager):

    def _create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email =models.EmailField(unique=True, blank=False)
    name = models.CharField(max_length=30, blank=False)
    last_name= models.CharField(max_length=30, blank=False)
    phone = PhoneNumberField(max_length=13, blank=False)
    date_joined=models.DateField(default=get_date,max_length=10)
    date_expired=models.DateField(max_length=10,null=True,blank=True)
    profile_image=models.ImageField(max_length=200,null=True,blank=True)
    company=models.ForeignKey(CompanyInfoModel,on_delete=models.CASCADE,null=True,blank=True)


    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return ('%s %s'% (self.name,self.last_name))

    def get_short_name(self):
        return self.name

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table='auth_user'

