# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse
from .models import DocumentInfoModel,LiabilityInfoModel
from .forms import DocumentInfoForm, LiabilityInfoForm

def add_document(request):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        new_id=str(int(DocumentInfoModel.objects.all().order_by('-document_id')[0].document_id)+1)
        formdocument=DocumentInfoForm(initial={'document_id':new_id})
        if request.method=='POST':
            formdocument=DocumentInfoForm(request.POST,request.FILES)
            if formdocument.is_valid():
                formdocument.save()
            return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'form':formdocument,'model_info':DocumentInfoModel,'title':'Yeni Dosya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def document_detail(request,document_id):
    if request.user.has_perm('document_panel.view_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id)
        return render(request, 'document_panel/detail_document.html', {'document':document,'title':'Dosya Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def table_document(request):
    if request.user.has_perm('document_panel.view_documentinfomodel'):
        document_list=DocumentInfoModel.objects.all()
        return render(request, 'document_panel/table_document.html', {'document_list':document_list,'title':'Dosya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def edit_document(request,document_id):
    if request.user.has_perm('document_panel.change_documentinfomodel'):
        formdocument = DocumentInfoForm(instance=DocumentInfoModel.objects.get(pk=document_id))
        if request.method=='POST':
            formdocument=DocumentInfoForm(request.POST,request.FILES,instance=DocumentInfoModel.objects.get(pk=document_id))
            if formdocument.is_valid():
                formdocument.save()
                return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'formdocument':formdocument,'model_info':DocumentInfoModel,'title':'Dosya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/home/')

def delete_document(request,document_id):
    if request.user.has_perm('document_panel.delete_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id)
        document.delete()
        return redirect('http://127.0.0.1:8000/document_panel/document_table/')
    else: return redirect('http://127.0.0.1:8000/home/')


def liability_add(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm()
        if request.POST:
            formliability=LiabilityInfoForm(request.POST)
            if formliability.is_valid():
                formliability.save()
                return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        return render(request,'document_panel/add_liability.html',{'form':formliability,'title':'Yeni Emanet kaydı','model_info':LiabilityInfoModel})
    else: return redirect('http://127.0.0.1:8000/home/')

def liability_detail(request,record_no):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no)
        return render(request,'document_panel/detail_liability.html',{'liability':liability,'title':'Emanet Detayı'})
    else: return redirect('http://127.0.0.1:8000/home/')

def liability_table(request):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.all()
        return render(request,'document_panel/table_liability.html',{'liability_list':liability_list,'title':'Emanet Tablosu'})
    else: return redirect('http://127.0.0.1:8000/home/')

def liability_edit(request,record_no):
    if request.user.has_perm('document_panel.change_liabilityinfomodel'):
        formliability=LiabilityInfoForm(instance=LiabilityInfoModel.objects.get(pk=record_no))
        if request.method=='POST':
            formliability=LiabilityInfoForm(request.POST,instance=LiabilityInfoModel.objects.get(pk=record_no))
            if formliability.is_valid():
                formliability.save()
            return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        return render(request,'document_panel/add_liability.html',{'form':formliability,'title':'Emanet Düzenleme','model_info':LiabilityInfoModel})
    else: return redirect('http://127.0.0.1:8000/home/')

def liability_delete(request,record_no):
    if request.user.has_perm('document_panel.delete_liabilityinfomodel'):
        LiabilityInfoModel.objects.get(pk=record_no).delete()
        return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
    else: return redirect('http://127.0.0.1:8000/home/')
