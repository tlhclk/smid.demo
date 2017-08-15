# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse
from .models import DocumentInfoModel,LiabilityInfoModel
from .forms import DocumentInfoForm, LiabilityInfoForm
from user_panel.models import UserCompanyModel,CompanyInfoModel

def add_document(request):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        new_id=str(int(DocumentInfoModel.objects.all().order_by('-document_id')[0].document_id)+1)
        formdocument=DocumentInfoForm(initial={'document_id':new_id})
        if request.method=='POST':
            formdocument=DocumentInfoForm(request.POST,request.FILES)
            if formdocument.is_valid():
                formdocument.save()
                document=DocumentInfoModel.objects.last()
                company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
                document.company_id=CompanyInfoModel.objects.get(pk=company_id)
                document.save()
            return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        person_list=DocumentInfoModel().person_list()
        document_type_list=DocumentInfoModel.document_type_list
        return render(request,'document_panel/add_document.html',{'form':formdocument,'person_list':person_list,'document_type_list':document_type_list,'title':'Yeni Dosya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def document_detail(request,document_id):
    if request.user.has_perm('document_panel.view_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id)
        if document.company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request, 'document_panel/detail_document.html', {'document':document,'title':'Dosya Detayı'})
        else: return redirect('http://127.0.0.1:8000/document_panel/document_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_document(request):
    if request.user.has_perm('document_panel.view_documentinfomodel'):
        document_list=DocumentInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request, 'document_panel/table_document.html', {'document_list':document_list,'title':'Dosya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_document(request,document_id):
    if request.user.has_perm('document_panel.change_documentinfomodel') and DocumentInfoModel.objects.get(pk=document_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        formdocument = DocumentInfoForm(instance=DocumentInfoModel.objects.get(pk=document_id))
        if request.method=='POST':
            formdocument=DocumentInfoForm(request.POST,request.FILES,instance=DocumentInfoModel.objects.get(pk=document_id))
            if formdocument.is_valid():
                formdocument.save()
                return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        person_list=DocumentInfoModel().person_list()
        document_type_list=DocumentInfoModel.document_type_list
        return render(request,'document_panel/add_document.html',{'form':formdocument,'person_list':person_list,'document_type_list':document_type_list,'title':'Dosya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_document(request,document_id):
    if request.user.has_perm('document_panel.delete_documentinfomodel') and DocumentInfoModel.objects.get(pk=document_id).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        document=DocumentInfoModel.objects.get(pk=document_id)
        document.delete()
        return redirect('http://127.0.0.1:8000/document_panel/document_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def liability_add(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm()
        if request.POST:
            formliability=LiabilityInfoForm(request.POST)
            if formliability.is_valid():
                formliability.save()
                liability=LiabilityInfoModel.objects.last()
                company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id
                liability.company_id=CompanyInfoModel.objects.get(pk=company_id)
                liability.save()
                return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        person_list=LiabilityInfoModel().person_list()
        liability_type_list=LiabilityInfoModel.fixture_type_list
        return render(request,'document_panel/add_liability.html',{'form':formliability,'title':'Yeni Emanet kaydı','person_list':person_list,'liability_type_list':liability_type_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_detail(request,record_no):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no)
        if liability.company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
            return render(request,'document_panel/detail_liability.html',{'liability':liability,'title':'Emanet Detayı'})
        else: return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_table(request):
    if request.user.has_perm('document_panel.view_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.filter(company_id=UserCompanyModel.objects.get(pk=request.user.id).company_id)
        return render(request,'document_panel/table_liability.html',{'liability_list':liability_list,'title':'Emanet Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_edit(request,record_no):
    if request.user.has_perm('document_panel.change_liabilityinfomodel') and LiabilityInfoModel.objects.get(pk=record_no).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        formliability=LiabilityInfoForm(instance=LiabilityInfoModel.objects.get(pk=record_no))
        if request.method=='POST':
            formliability=LiabilityInfoForm(request.POST,instance=LiabilityInfoModel.objects.get(pk=record_no))
            if formliability.is_valid():
                formliability.save()
            return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        person_list = LiabilityInfoModel().person_list()
        liability_type_list = LiabilityInfoModel.fixture_type_list
        return render(request, 'document_panel/add_liability.html',{'form': formliability, 'title': 'Emanet Düzenleme', 'person_list': person_list,'liability_type_list': liability_type_list})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_delete(request,record_no):
    if request.user.has_perm('document_panel.delete_liabilityinfomodel') and LiabilityInfoModel.objects.get(pk=record_no).company_id.company_id == UserCompanyModel.objects.get(pk=request.user.id).company_id:
        LiabilityInfoModel.objects.get(pk=record_no).delete()
        return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')
