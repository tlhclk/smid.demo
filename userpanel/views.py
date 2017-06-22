# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import(authenticate,login,logout)
from django.contrib.auth.models import User,Group,Permission,ContentType
from .forms import UserLoginForm,UserRegistrationForm,PermissionForm,UserPermissionForm,GroupPermissionForm,RemoverForm,AddGroup


def options_menu(request):
    return render(request,'user_panel/options_menu.html')

def log_in(request):
    user = 'None'
    title='Login'
    form = UserLoginForm(request.POST or None)
    if str(request.user) == 'AnonymousUser':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../')

        #return render(request, "user_panel/deneme.html", {"form": form,'user': user,'title':title})
        #return render(request, "user_panel/login.html", {"form": form, 'user': user, 'title': title})
        return render(request,'staticasdqW/pages/examples/login.html',{'form':form})
    else:
        return HttpResponse('Already an user singed in: ' + str(request.user))

def log_out(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
    return redirect('../../')

def user_add(request):#register
    if request.user.has_perm('auth.add_user'):
        if request.method=='POST':
            form = UserRegistrationForm(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                user.set_password(password)
                user.username=form.cleaned_data.get('email')
                user.save()
        return render(request, "user_panel/register.html")
    else:
        return HttpResponse('You has no autharization to add user')

def user_detail(request,user_id):
    if request.user.has_perm('auth.view_user'):
        user=User.objects.get(pk=user_id)
        if str(user.username) != 'AnonymousUser':
            return render(request,'user_panel/user_detail.html',{'user':user})
        else: return HttpResponse('You are Anonymous,you have nothing')
    else: return HttpResponse('You has no authorization to view user detail')

def user_table(request):
    if 1==1:
        user_list=User.objects.all()
        return render(request,'user_panel/user_table.html',{'user_list':user_list})
    else: return HttpResponse('You has no authorization to view user table')

def user_delete(request,user_id):
    if request.user.has_perm('auth.delete_user'):
        user=User.objects.get(pk=user_id)
        user.delete()
        return redirect('../../user_table/')
    else: return HttpResponse('You has no authorization to delete user')

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

def group_detail(request,group_id):
    if request.user.has_perm('auth.view_group'):
        group=Group.objects.get(pk=group_id)
        user_list=User.objects.filter(groups=group)
        return render(request,'user_panel/group_detail.html',{'group':group,'user_list':user_list,'group_perm':group.permissions.all()})
    else: return HttpResponse('You has no authorization to view group detail')

def group_table(request):
    if request.user.has_perm('auth.view_group'):
        group_list=Group.objects.all()
        return render(request,'user_panel/group_table.html',{'group_list':group_list})
    else: return HttpResponse('You has no authorization to view group table')

def group_delete(request,group_id):
    if request.user.has_perm('auth.delete_group'):
        group=Group.objects.get(pk=group_id)
        group.delete()
        return redirect('../../group_table/')
    else: return HttpResponse('You has no authorization to delete group')

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

def permission_table(request):
    if request.user.has_perm('auth.view_permission'):
        permission_list=Permission.objects.all()
        return render(request,'user_panel/permission_table.html',{'permission_list':permission_list,'content_type':ContentType})
    else: return HttpResponse('You have no authorization to view permission table')

def permission_delete(request,permission_id):
    if request.user.has_perm('auth.delete_permission'):
        permission=Permission.objects.get(pk=permission_id)
        permission.delete()
        return redirect('../../permission_table/')
    else: return HttpResponse('You have no authorization to delete permission')

def remover(request):
    title='Remover'
    form = RemoverForm(request.POST or None)
    if form.is_valid():
        remover_choice = form.cleaned_data.get('remover_choice')
        if remover_choice=='1':
            if request.user.has_perm('auth.delete_user'):
                user_id = form.cleaned_data.get('user_choice')
                print (user_id)
                selection = User.objects.get(pk=user_id)
                selection.delete()
            else: return HttpResponse('You has no authorization to delete any user')
        elif remover_choice=='2':
            if request.user.has_perm('auth.delete_permission'):
                permission_id = form.cleaned_data.get('permission_choice')
                print (permission_id)
                selection = Permission.objects.get(pk=permission_id)
                selection.delete()
            else: return HttpResponse('You has no authorization to delete any permission')
        elif remover_choice=='3':
            if request.user.has_perm('auth.delete_group'):
                group_id = form.cleaned_data.get('group_choice')
                print (group_id)
                selection = Group.objects.get(pk=group_id)
                selection.delete()
            else: return HttpResponse('You has no authorization to delete any group')
        else: pass
    return render(request,'user_panel/default_form.html',{'form':form,'title':title})

def user_permission_add(request):
    if request.user.has_perm('auth.change_permission'):
        title='User Permission Add'
        form = UserPermissionForm(request.POST or None)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_choice')
            permission_list=form.cleaned_data.get('permission_choice')
            user = User.objects.get(pk=user_id)
            for per in permission_list[1]:
                permission = Permission.objects.get(pk=per)
                content = ContentType.objects.get(pk=permission.content_type_id)
                if user.has_perm('%s.%s'%(content.app_label,permission.codename)):
                    print (user,per,'already has')
                    pass
                else:
                    user.user_permissions.add(per)

        return render(request,'user_panel/default_form.html',{'form':form,'title':title})
    else:
        return HttpResponse('has no auth for changing permissions')

def group_permission_add(request):
    if request.user.has_perm('auth.change_permission'):
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
                    pass
                else:
                    print permission.codename,'given'
                    group.permissions.add(per)
            return redirect('../group_table')
        return render(request,'user_panel/default_form.html',{'form':form,'title':title})
    else: return HttpResponse('has no auth for changing permissions, changing groups: '+str(request.user))

def group_user_edit(request):
    pass

def user_edit(request,user_id):
    if request.user.has_perm('auth.change_user'):
        user=User.objects.get(pk=user_id)
        if request.method=='POST':
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.email=request.POST['email']
            user.password=request.POST['password']
            user.password_check=request.POST['password2']
            group_choice=request.POST['group_choice']
            group=Group.objects.get(pk=user.groups.all()[0].id)
            group.user_set.remove(user)
            user.groups.add(group_choice)
            return redirect('../../user_table/')
        return render(request,'user_panel/edit_user.html',{'user':user})


    else: return HttpResponse('You has no authorization to edit a user profile')