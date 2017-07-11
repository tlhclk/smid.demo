# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import(authenticate,login,logout)
from django.contrib.auth.models import User,Group,Permission,ContentType
from .forms import UserLoginForm,UserRegistrationForm,PermissionForm,GroupPermissionForm,AddGroup


def option_menu(request):
    return render(request,'user_panel/option_menu.html')

def log_in(request):
    if str(request.user) == 'AnonymousUser':
        formuser = UserLoginForm(request.POST or None)
        if request.method=='POST':
            if formuser.is_valid():
                username = formuser.cleaned_data.get("username")
                password = formuser.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('../')

        return render(request,'user_panel/default_form.html',{'form':formuser})
    else:
        return HttpResponse('Already an user singed in: ' + str(request.user))

def log_out(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
    return redirect('../../')

def add_user(request):#register
    if request.user.has_perm('auth.add_user'):
        formuser = UserRegistrationForm()
        if request.method=='POST':
            formuser = UserRegistrationForm(request.POST)
            if formuser.is_valid():
                user = formuser.save(commit=False)
                password = formuser.cleaned_data.get('password')
                user.set_password(password)
                user.username=formuser.cleaned_data.get('email')
                user.save()
        return render(request, "user_panel/default_form.html",{'form':formuser})
    else:
        return HttpResponse('You has no autharization to add user')

def detail_user(request,user_id):
    if request.user.has_perm('auth.view_user'):
        if str(request.user) != 'AnonymousUser':
            user=User.objects.get(pk=user_id)
            return render(request,'user_panel/detail_user.html',{'user':user})
        else: return HttpResponse('You are Anonymous,you have nothing')
    else: return HttpResponse('You has no authorization to view user detail')

def edit_user(request, user_id):
    if request.user.has_perm('auth.change_user'):
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
    if request.user.has_perm('auth.view_user'):
        user_list=User.objects.all()
        return render(request,'user_panel/table_user.html',{'user_list':user_list})
    else: return HttpResponse('You has no authorization to view user table')

def delete_user(request,user_id):
    if request.user.has_perm('auth.delete_user'):
        User.objects.get(pk=user_id).delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to delete user')

def detail_group(request,group_id):
    if request.user.has_perm('auth.view_group'):
        group=Group.objects.get(pk=group_id)
        user_list=User.objects.filter(groups=group)
        return render(request,'user_panel/detail_group.html',{'group':group,'user_list':user_list,'group_perm':group.permissions.all()})
    else: return HttpResponse('You has no authorization to view group detail')

def table_group(request):
    if request.user.has_perm('auth.view_group'):
        group_list=Group.objects.all()
        return render(request,'user_panel/table_group.html',{'group_list':group_list})
    else: return HttpResponse('You has no authorization to view group table')

def table_permission(request):
    if request.user.has_perm('auth.view_permission'):
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
            print permission_list
            group = Group.objects.get(pk=group_id)
            for per in permission_list[1]:
                permission = Permission.objects.get(pk=per)
                if permission in group.permissions.all():
                    print permission,'already has'
                else:
                    print permission.codename,'given'
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
