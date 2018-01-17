# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import (render_to_response)
from django.template import RequestContext
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import(authenticate,login,logout)
from django.contrib.auth.models import Group,Permission,ContentType
from .forms import UserLoginForm,UserRegistrationForm,CompanyInfoForm,FreeRegisterForm
from .models import CompanyInfoModel,User
from operation_panel.views import notification



def add_user(request):#TODO: şuan askıdan dğzenlencek veya silinecek
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
    if request.user.has_perm('user_panel.change_user'):
        user=User.objects.get(pk=user_id,company=request.user.company)
        return render(request,'user_panel/detail_user.html',{'user':user})
    else: return HttpResponse('You has no authorization to view user detail')

def edit_user(request, user_id):
    if request.user.has_perm('user_panel.add_user'):
        auser=User.objects.get(pk=user_id,company=request.user.company_id)
        formuser= UserRegistrationForm(instance=auser)
        if request.method=='POST':
            formuser = UserRegistrationForm(request.POST,instance=auser)
            if formuser.is_valid():
                formuser.save()
                return redirect('http://127.0.0.1:8000/user_panel/user_table/')
        return render(request, 'user_panel/default_form.html', {'form': formuser})
    else:
        return HttpResponse('You has no authorization to edit a user profile')

def table_user(request):
    if request.user.has_perm('user_panel.change_user'):
        user_list=User.objects.filter(company=request.user.company_id)
        return render(request,'user_panel/table_user.html',{'user_list':user_list})
    else: return HttpResponse('You has no authorization to view user table')

def delete_user(request,user_id):
    if request.user.has_perm('user_panel.add_user'):
        User.objects.get(pk=user_id,company=request.user.company_id).delete()
        return redirect('http://127.0.0.1:8000/user_panel/user_table/')
    else: return HttpResponse('You has no authorization to delete user')


def add_company(request):
    if request.user.has_perm('user_panel.add_companyinfomodel'):
        if request.method=='POST':
            formcompany = CompanyInfoForm(request.POST)
            if formcompany.is_valid():
                formcompany.save()
                return redirect('http://127.0.0.1:8000/home/')
        formcompany=CompanyInfoForm()
        return render(request,'user_panel/add_company.html',{'formcompany':formcompany,'title':'Yeni Yurt Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def detail_company(request,company_id):
    if request.user.has_perm('user_panel.change_companyinfomodel'):
        company=CompanyInfoModel.objects.get(pk=company_id)
        return render(request,'user_panel/detail_company.html',{'title':'Yurt Detayları','company':company})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_company(request):
    if request.user.has_perm('user_panel.change_companyinfomodel'):
        company_list=CompanyInfoModel.objects.all()
        return render(request, 'user_panel/table_company.html', {'title': 'Yurtlar Tablosu', 'company_list': company_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_company(request,company_id):
    if request.user.has_perm('user_panel.add_companyinfomodel'):
        if request.method=='POST':
            formcompany = CompanyInfoForm(request.POST,CompanyInfoModel.objects.get(pk=company_id))
            if formcompany.is_valid():
                formcompany.save()
                return redirect('http://127.0.0.1:8000/home/')
        formcompany=CompanyInfoForm(CompanyInfoModel.objects.get(pk=company_id))
        return render(request,'user_panel/add_company.html',{'formcompany':formcompany,'title':'Yeni Yurt Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_company(request,company_id):
    if request.user.has_perm('user_panel.add_companyinfomodel'):
        CompanyInfoModel.objects.get(pk=company_id).delete()
        return redirect('http://127.0.0.1:8000/user_panel/user_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


from django.views.decorators.csrf import csrf_exempt


def log_in(request):
    if not request.user.id:
        print(request.COOKIES)
        formuser = UserLoginForm()
        if request.method=='POST':
            formuser=UserLoginForm(request.POST)
            print(formuser)
            print(request.POST['password'])
            if formuser.is_valid():
                print(request.POST['password'])
                email = formuser.cleaned_data.get("email")
                password = formuser.cleaned_data.get("password")
                user = authenticate(email=email, password=password)
                print(user)
                login(request, user)
                print(login(request, user))
                #notification(request)
                return redirect('http://127.0.0.1:8000/home/')
        return render(request,'user_panel/login.html',{'form':formuser})
    else:
        return redirect('http://127.0.0.1:8000/home/')

def log_out(request):
    if request.user.id:
        logout(request)
    return redirect('http://127.0.0.1:8000/')

def register(request):
    if not request.user.id:
        formuser = FreeRegisterForm()
        if request.method == 'POST':
            formuser = FreeRegisterForm(request.POST)
            if formuser.is_valid():
                formuser.save()
                return redirect('http://127.0.0.1:8000/home/')
        return render(request, "user_panel/register.html", {'form': formuser,'title':'Dormoni Ücretsiz Kayıt'})
    else:
        return redirect('http://127.0.0.1:8000/home/')
