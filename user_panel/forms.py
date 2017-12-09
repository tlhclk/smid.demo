# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group,Permission,ContentType
from django.contrib.auth import (authenticate, get_user_model, password_validation)
from .models import CompanyInfoModel,UserCompanyModel,User
from phonenumber_field.formfields import PhoneNumberField
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
            'company_id'
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
    name = forms.CharField(label='Ad')
    last_name= forms.CharField(label='Soyad')
    password = forms.CharField(widget=forms.PasswordInput(), label='Şifre',strip=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Şifre Tekrar',strip=False)
    termofuse= forms.BooleanField(widget=forms.CheckboxInput(),label='<a href="https://dormoni.com/termofuse/" >Kullanım Koşullarını</a> Kabul Ediyorum')

    class Meta:

        fields = [
            'email',
            'name',
            'last_name',
            'password',
            'password2',
            'phone',
            'termofuse',
        ]

    def clean(self):
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            self.add_error('password2',"Şifre Uyuşmuyor")
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)

    def company_id(self):
        id=str(int(CompanyInfoModel.objects.last().company_id)+1)
        new_temp_comp=CompanyInfoModel(company_id=id,company_name='new_temp_%s'%id,company_vno='0')
        new_temp_comp.save()
        return new_temp_comp

    def date_expired(self):
        return datetime.date.today()+datetime.timedelta(days=15)

    def save(self):
        new_user=User(email=self.cleaned_data.get('email'),name=self.cleaned_data.get('name'),last_name=self.cleaned_data.get('last_name'),phone=self.cleaned_data.get('phone'),date_expired=self.date_expired(),company_id=self.compony_id())
        new_user.set_password(self.cleaned_data.get('password'))
        new_user.groups.add(3)
        new_user.save()



class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email Adresi',widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        usr=User.objects.get(email=email)
        if usr:
            if datetime.datetime.today().date()>usr.date_expired:
                if datetime.datetime.today().date()-usr.date_expired> datetime.timedelta(days=7):
                    comp=CompanyInfoModel.objects.get(company_id=usr.company_id_id)
                    usr.delete()
                    comp.delete()

                self.add_error('email','Kullandığınız Mail Adresinin Kullanım Süresi Dolmuştur. Lütfen Üyeliğinizi Güncelleyiniz.')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                self.add_error('email',"Boyle bir kullanici yok ya da şifre hatalı")
                self.add_error('password','Boyle bir kullanici yok ya da şifre hatalı')
            return super(UserLoginForm, self).clean()

class ChangePasswordForm(forms.Form):
    email=forms.EmailField(label='E-Posta',widget=forms.EmailInput())
    class Meta:
        fields=['email']

    def clean(self):
        email=self.cleaned_data.get('email')
        if email in User.objects.all():
            pass
        else:
            self.add_error('Yanlış E-Posta Adresi Girdiniz')

class PermissionForm(forms.ModelForm):
    content_list = []
    for content in ContentType.objects.all():
        content_list.append((content.id, content.name))
    content_type_id = forms.ChoiceField(label='Content', choices=content_list, required=False)
    codename = forms.CharField(label='Permission Codename')
    name = forms.CharField(label='Permission Description')
    class Meta:
        model=Permission
        fields=['content_type_id','codename','name',]
    def clean(self):
        content = self.cleaned_data.get('content_type_id')
        permission_c = self.cleaned_data.get('codename')
        permission_list = Permission.objects.filter(content_type=content)
        for permis in permission_list:
            if permis.codename == permission_c:
                raise forms.ValidationError(
                    'There is a permission in selected content: %s, %s' % (content, permission_c))
        return self.cleaned_data


class GroupPermissionForm(forms.Form):
    permission_list = []
    for per in Permission.objects.all():
        permission_list.append((per.id, per.name))
    group_list = []
    for group in Group.objects.all():
        group_list.append((group.id, group.name))

    group_choice = forms.ChoiceField(label='Group', choices=group_list, required=False,initial='2')
    permission_choice = forms.MultipleChoiceField(label='Permissions', widget=forms.CheckboxSelectMultiple,choices=permission_list, required=False)

    def clean_permission_choice(self):
        group_id = self.cleaned_data.get('group_choice')
        permission_list = self.cleaned_data.get('permission_choice')
        kullanici = Group.objects.get(pk=group_id)
        #for per in permission_list:
           #if kullanici.has_perm(per):
               #raise forms.ValidationError('user already has the permission %s'%per)
        return group_id, permission_list


class AddGroup(forms.Form):
    group_name=forms.CharField(label='Group Name',)
    class Meta:
        model=Group
        fields=['group_name']

class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model=CompanyInfoModel
        fields=['company_id',
                'company_name',
                'company_vno',
                'company_adress',
                'company_account_no',
                'company_payment_detail',
                'company_desc'
                ]

class UserCompanyForm(forms.ModelForm):
    class Meta:
        model=UserCompanyModel
        fields=['user',
                'company']

