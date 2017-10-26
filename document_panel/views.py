# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse
from .models import DocumentInfoModel,LiabilityInfoModel
from .forms import DocumentInfoForm, LiabilityInfoForm
from user_panel.models import UserCompanyModel,CompanyInfoModel
from person_panel.models import StudentInfoModel

def add_document(request):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        formdocument=DocumentInfoForm(user=request.user)
        if request.method=='POST':
            formdocument=DocumentInfoForm(user=request.user,POST=request.POST,FILES=request.FILES)
            if formdocument.is_valid():
                formdocument.save()
            return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'form':formdocument,'title':'Yeni Dosya Kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def document_detail(request,document_id):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id)
        if document.company_id.company_id == request.user.company_id_id:
            return render(request, 'document_panel/detail_document.html', {'document':document,'title':'Dosya Detayı'})
        else: return redirect('http://127.0.0.1:8000/document_panel/document_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def table_document(request,student_id):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        document_list=DocumentInfoModel.objects.filter(company_id=request.user.company_id_id)
        if student_id: document_list=document_list.filter(person_id=student_id)
        return render(request, 'document_panel/table_document.html', {'document_list':document_list,'title':'Dosya Tablosu'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def edit_document(request,document_id):
    document=DocumentInfoModel.objects.get(pk=document_id)
    if request.user.has_perm('document_panel.change_documentinfomodel') and document.company_id_id == request.user.company_id_id:
        formdocument = DocumentInfoForm(user=request.user,instance=document,initial={'image_field':document.image_field})
        if request.method=='POST':
            formdocument=DocumentInfoForm(user=request.user,POST=request.POST,FILES=request.FILES,instance=DocumentInfoModel.objects.get(pk=document_id))
            if formdocument.is_valid():
                formdocument.save()
                return redirect('http://127.0.0.1:8000/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'form':formdocument,'title':'Dosya Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def delete_document(request,document_id):
    if request.user.has_perm('document_panel.delete_documentinfomodel') and DocumentInfoModel.objects.get(pk=document_id).company_id.company_id == request.user.company_id_id:
        document=DocumentInfoModel.objects.get(pk=document_id)
        document.delete()
        return redirect('http://127.0.0.1:8000/document_panel/document_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')


def liability_add(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm(user=request.user)
        if request.POST:
            formliability=LiabilityInfoForm(user=request.user,POST=request.POST)
            if formliability.is_valid():
                formliability.save()
                return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        return render(request,'document_panel/add_liability.html',{'form':formliability,'title':'Yeni Emanet kaydı'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_detail(request,record_no):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no)
        if liability.company_id.company_id == request.user.company_id_id:
            return render(request,'document_panel/detail_liability.html',{'liability':liability,'title':'Emanet Detayı'})
        else: return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_table(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.filter(company_id=request.user.company_id_id)
        return render(request,'document_panel/table_liability.html',{'liability_list':liability_list,'title':'Eşya Bilgileri'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_edit(request,record_no):
    if request.user.has_perm('document_panel.change_liabilityinfomodel') and LiabilityInfoModel.objects.get(pk=record_no).company_id.company_id == request.user.company_id_id:
        formliability=LiabilityInfoForm(user=request.user,instance=LiabilityInfoModel.objects.get(pk=record_no))
        if request.method=='POST':
            formliability=LiabilityInfoForm(user=request.user,POST=request.POST,instance=LiabilityInfoModel.objects.get(pk=record_no))
            if formliability.is_valid():
                formliability.save()
            return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
        return render(request, 'document_panel/add_liability.html',{'form': formliability, 'title': 'Emanet Düzenleme'})
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')

def liability_delete(request,record_no):
    if request.user.has_perm('document_panel.delete_liabilityinfomodel') and LiabilityInfoModel.objects.get(pk=record_no).company_id.company_id == request.user.company_id_id:
        LiabilityInfoModel.objects.get(pk=record_no).delete()
        return redirect('http://127.0.0.1:8000/document_panel/liability_table/')
    else: return redirect('http://127.0.0.1:8000/user_panel/login/')
