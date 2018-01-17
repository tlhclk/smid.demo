# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import (authenticate, get_user_model, password_validation)
from .models import CompanyInfoModel,ChainCompanyInfoModel,User
from phonenumber_field.formfields import PhoneNumberField
from django.core import mail
import datetime

UserModel=get_user_model()


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adresi',widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput, label='Şifre',strip=False)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Şifre Tekrar',strip=False)

    class Meta:
        model = UserModel
        fields = [
            'email',
            'name',
            'last_name',
            'password',
            'password2',
            'phone',
            'profile_image',
            'company'
        ]

    def clean(self):
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            self.add_error('password2',"The two password fields didn't match.")
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)


class FreeRegisterForm(forms.Form):
    email = forms.EmailField(label='Email Adresi',widget=forms.EmailInput())
    name = forms.CharField(label='Ad',max_length=50)
    last_name= forms.CharField(label='Soyad',max_length=50)
    phone = PhoneNumberField(label='Telefon Numarası')
    termofuse= forms.BooleanField(widget=forms.CheckboxInput(),label='<a href="https://dormoni.com/termofuse/" >Kullanım Koşullarını</a> Kabul Ediyorum')

    class Meta:
        fields = [
            'email',
            'name',
            'last_name',
            'phone',
            'termofuse',
        ]

    def company(self):
        id=str(int(CompanyInfoModel.objects.last().company)+1)
        new_temp_comp=CompanyInfoModel(company=id,company_name='new_temp_%s'%id,company_vno='0')
        new_temp_comp.save()
        return new_temp_comp

    def date_expired(self):
        return datetime.date.today()+datetime.timedelta(days=15)

    def save(self):
        new_user=User(email=self.cleaned_data.get('email'),name=self.cleaned_data.get('name'),last_name=self.cleaned_data.get('last_name'),phone=self.cleaned_data.get('phone'),date_expired=self.date_expired(),company=self.company())
        new_pass=User.objects.make_random_password()
        new_user.set_password(new_pass)
        new_user.save()
        new_user.groups.add(3)
        new_user.save()
        subj = 'Yeni Kayıt'
        mesg = 'Merhablar\n\nSistemimize kayıt olduğunuz için teşekkür ederiz.\nKullanıcı bilgileriniz:\nEmail = %s \nŞifreniz: %s\nSisteme Bu <a href="https://dormoni.com">Adresten</a> Giriş Yapabilirsiniz.\n15 Günlük Deneme Sürümünü Kullanıyorsunuz.\n\t-15 gün sonra kayıt yada düzenleme işlemlerini yapamayacaksınız.\n\t-45 gün sonra yaptığınız bütün işlemler silinecektir.' % (self.cleaned_data.get('email'), new_pass)
        mail.send_mail(subj, mesg,'admin@dormoni.com',[self.cleaned_data.get('email')])


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email Adresi',widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     if email and password:
    #         user = authenticate(email=email, password=password)
    #         if not user:
    #             self.add_error('email',"Boyle bir kullanici yok ya da şifre hatalı")
    #             self.add_error('password','Boyle bir kullanici yok ya da şifre hatalı')
    #         return super(UserLoginForm, self).clean()

class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model=CompanyInfoModel
        fields=['name',
                'vno',
                'address',
                'account',
                'payment_detail',
                'chain_company',
                'desc'
                ]

class ChainCompanyInfoForm(forms.ModelForm):
    class Meta:
        model=ChainCompanyInfoModel
        fields=['name',
                'person',
                'phone',
                'email'
                ]

