# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import (render_to_response)
from django.template import RequestContext
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import(authenticate,login,logout)
from django.contrib.auth.models import Group,Permission,ContentType
from .forms import UserLoginForm,UserRegistrationForm,PermissionForm,GroupPermissionForm,AddGroup,CompanyInfoForm,FreeRegisterForm
from .models import CompanyInfoModel,User
from django.contrib.auth import views as auth_views



def log_in(request):
    if str(request.user) == 'AnonymousUser':
        formuser = UserLoginForm()
        if request.method=='POST':
            formuser=UserLoginForm(request.POST)
            if formuser.is_valid():
                email = formuser.cleaned_data.get("email")
                password = formuser.cleaned_data.get("password")
                remember = formuser.cleaned_data.get("remember")
                user = authenticate(email=email, password=password)
                login(request, user)
                if remember==True:
                    request.session.set_expiry(604800)#bir haftalık
                else:
                    request.session.set_expiry(0)
                return redirect('https://dormoni.com/home/')

        return render(request,'user_panel/login.html',{'form':formuser})
    else:
        return redirect('https://dormoni.com/home/')

def log_out(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
    return redirect('https://dormoni.com/')

def register(request):
    if not request.user.id:
        formuser = FreeRegisterForm()
        if request.method == 'POST':
            formuser = FreeRegisterForm(request.POST)
            print(formuser)
            if formuser.is_valid():
                formuser.save()
                return redirect('https://dormoni.com/home/')
        return render(request, "user_panel/register.html", {'form': formuser,'title':'Dormoni Ücretsiz Kayıt'})
    else:
        return redirect('https://dormoni.com/home/')

def add_user(request):
    if request.user.has_perm('user_panel.add_user'):
        formuser = UserRegistrationForm()
        if request.method=='POST':
            formuser = UserRegistrationForm(request.POST)
            if formuser.is_valid():
                user = formuser.save(commit=False)
                password = formuser.cleaned_data.get('password')
                user.set_password(password)
                user.save()
        return render(request, "user_panel/default_form.html",{'form':formuser})
    else:
        return redirect('home')

def detail_user(request,user_id):
    if request.user.has_perm('user_panel.add_user'):
        if str(request.user) != 'AnonymousUser':
            user=User.objects.get(pk=user_id)
            return render(request,'user_panel/detail_user.html',{'user':user})
        else: return HttpResponse('You are Anonymous,you have nothing')
    else: return HttpResponse('You has no authorization to view user detail')

def edit_user(request, user_id):
    if 1==1:#request.user.has_perm('user_panel.change_user'):
        formuser= UserRegistrationForm(instance=User.objects.get(pk=user_id))
        if request.method=='POST':
            formuser = UserRegistrationForm(request.POST,instance=User.objects.get(pk=user_id))
            if formuser.is_valid():
                formuser.save()
                return redirect('../')
        return render(request, 'user_panel/default_form.html', {'form': formuser})
    else:
        return HttpResponse('You has no authorization to edit a user profile')

def table_user(request):
    if request.user.has_perm('user_panel.add_user'):
        user_list=User.objects.all()
        return render(request,'user_panel/table_user.html',{'user_list':user_list})
    else: return HttpResponse('You has no authorization to view user table')

def delete_user(request,user_id):
    if request.user.has_perm('user_panel.delete_user'):
        User.objects.get(pk=user_id).delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to delete user')

def detail_group(request,group_id):
    if request.user.has_perm('auth.add_group'):
        group=Group.objects.get(pk=group_id)
        user_list=User.objects.filter(groups=group)
        return render(request,'user_panel/detail_group.html',{'group':group,'user_list':user_list,'group_perm':group.permissions.all()})
    else: return HttpResponse('You has no authorization to view group detail')

def table_group(request):
    if request.user.has_perm('auth.add_group'):
        group_list=Group.objects.all()
        return render(request,'user_panel/table_group.html',{'group_list':group_list})
    else: return HttpResponse('You has no authorization to view group table')

def table_permission(request):
    if request.user.has_perm('auth.add_permission'):
        permission_list=Permission.objects.all()
        return render(request,'user_panel/table_permission.html',{'permission_list':permission_list,'content_type':ContentType})
    else: return HttpResponse('You have no authorization to view permission table')

def permission_add(request):
    if request.user.has_perm('auth.add_permission'):
        title='Permission Add'
        form =PermissionForm()
        if request.method=='POST':
            form = PermissionForm(request.POST or None)
            if form.is_valid():
                content = form.cleaned_data.get('content_type_id')
                permission_desc = form.cleaned_data.get('name')
                permission_codename = form.cleaned_data.get('codename')
                new_permission = Permission(name=permission_desc,codename=permission_codename,content_type_id=content)
                new_permission.save()
        return render(request, 'user_panel/default_form.html', {'form': form,'title':title})
    else: return HttpResponse('You have no authorization to create new permission')

def group_permission_add(request):
    if 1==1:#request.user.has_perm('auth.change_permission'):
        title='Group Permssion Add'
        form = GroupPermissionForm(request.POST or None)
        if form.is_valid():
            group_id = form.cleaned_data.get('group_choice')
            permission_list = form.cleaned_data.get('permission_choice')
            group = Group.objects.get(pk=group_id)
            for per in permission_list[1]:
                permission = Permission.objects.get(pk=per)
                if permission in group.permissions.all():
                    print (permission,'already has')
                else:
                    group.permissions.add(per)
            return redirect('../group_table')
        return render(request,'user_panel/default_form.html',{'form':form,'title':title})
    else: return HttpResponse('has no auth for changing permissions, changing groups: '+str(request.user))

def add_group(request):
    if request.method=='POST':
        group_form=AddGroup(request.POST)
        if group_form.is_valid():
            group_name=group_form.cleaned_data.get('group_name')
            new_group=Group(name=group_name)
            new_group.save()
            return redirect('../')
    group_form=AddGroup()
    return render(request,'user_panel/default_form.html',{'form':group_form})


def add_company(request):
    if 1==1:#request.user.has_perm('user_panel.add_companyinfomodel'):
        if request.method=='POST':
            formcompany = CompanyInfoForm(request.POST)
            if formcompany.is_valid():
                formcompany.save()
                return redirect('https://dormoni.com/home/')
        formcompany=CompanyInfoForm()
        return render(request,'user_panel/add_company.html',{'formcompany':formcompany,'title':'Yeni Yurt Kaydı'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def detail_company(request,company_id):
    if request.user.has_perm('user_panel.add_companyinfomodel'):
        company=CompanyInfoModel.objects.get(pk=company_id)
        return render(request,'user_panel/detail_company.html',{'title':'Yurt Detayları','company':company})
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_company(request):
    if request.user.has_perm('user_panel.add_companyinfomodel'):
        company_list=CompanyInfoModel.objects.all()
        return render(request, 'user_panel/table_company.html', {'title': 'Yurtlar Tablosu', 'company_list': company_list})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_company(request,company_id):
    if request.user.has_perm('user_panel.change_companyinfomodel'):
        if request.method=='POST':
            formcompany = CompanyInfoForm(request.POST,CompanyInfoModel.objects.get(pk=company_id))
            if formcompany.is_valid():
                formcompany.save()
                return redirect('https://dormoni.com/home/')
        formcompany=CompanyInfoForm(CompanyInfoModel.objects.get(pk=company_id))
        return render(request,'user_panel/add_company.html',{'formcompany':formcompany,'title':'Yeni Yurt Kaydı'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_company(request,company_id):
    if request.user.has_perm('user_panel.delete_companyinfomodel'):
        CompanyInfoModel.objects.get(pk=company_id).delete()
    else: return redirect('https://dormoni.com/user_panel/login/')
