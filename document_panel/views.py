# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse
from .models import DocumentInfoModel,LiabilityInfoModel
from .forms import DocumentInfoForm, LiabilityInfoForm



def option_menu(request):
    return render(request,'document_panel/option_menu.html')

def add_document(request):
    formdocument=DocumentInfoForm()
    if request.method=='POST':
        formdocument=DocumentInfoForm(request.POST,request.FILES)
        if formdocument.is_valid():
            formdocument.save()
        return redirect('../../')
    return render(request,'document_panel/default_form.html',{'form':formdocument})

def document_detail(request,document_id):
    document=DocumentInfoModel.objects.get(pk=document_id)
    return render(request, 'document_panel/detail_document.html', {'document':document})

def table_document(request):
    document_list=DocumentInfoModel.objects.all()
    return render(request, 'document_panel/table_document.html', {'document_list':document_list})

def edit_document(request,document_id):
    formdocument = DocumentInfoForm(instance=DocumentInfoModel.objects.get(pk=document_id))
    if request.method=='POST':
        formdocument=DocumentInfoForm(request.POST,request.FILES,instance=DocumentInfoModel.objects.get(pk=document_id))
        if formdocument.is_valid():
            formdocument.save()
            return redirect('../../')
    return render(request,'document_panel/default_form.html',{'form':formdocument})

def delete_document(request,document_id):
    document=DocumentInfoModel.objects.get(pk=document_id)
    document.delete()
    return redirect('../../')


def liability_add(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm()
        if request.POST:
            formliability=LiabilityInfoForm(request.POST)
            if formliability.is_valid():
                formliability.save()
                return redirect('../')
        return render(request,'user_panel/default_form.html',{'form':formliability})
    else: return HttpResponse('You has no authorization to change room info')

def liability_detail(request,record_no):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no)
        return render(request,'document_panel/detail_liability.html',{'liability':liability})
    else: return HttpResponse('You has no authorization to change room info')

def liability_table(request):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.all()
        return render(request,'document_panel/table_liability.html',{'liability_list':liability_list})
    else: return HttpResponse('You has no authorization to change room info')

def liability_edit(request,record_no):
    if request.user.has_perm('document_panel.change_liabilityinfomodel'):
        formliability=LiabilityInfoForm(instance=LiabilityInfoModel.objects.get(pk=record_no))
        if request.POST:
            formliability=LiabilityInfoForm(request.POST,instance=LiabilityInfoModel.objects.get(pk=record_no))
            if formliability.is_valid():
                formliability.save()
            return redirect('../')
        return render(request,'user_panel/default_form.html',{'form':formliability,'title':'Edit'})
    else: return HttpResponse('You has no authorization to change room info')

def liability_delete(request,record_no):
    if request.user.has_perm('document_panel.delete_liabilityinfomodel'):
        LiabilityInfoModel.objects.get(pk=record_no).delete()
        return redirect('../')
    else: return HttpResponse('You has no authorization to change room info')
