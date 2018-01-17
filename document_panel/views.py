# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,HttpResponse
from .models import DocumentInfoModel,LiabilityInfoModel
from .forms import DocumentInfoForm, LiabilityInfoForm
from user_panel.models import CompanyInfoModel
from person_panel.models import StudentInfoModel

def add_document(request):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        formdocument=DocumentInfoForm(user=request.user)
        if request.method=='POST':
            formdocument=DocumentInfoForm(user=request.user,POST=request.POST,FILES=request.FILES)
            if formdocument.is_valid():
                formdocument.save()
            return redirect('https://dormoni.com/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'form':formdocument,'title':'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def document_detail(request,document_id):
    if request.user.has_perm('document_panel.change_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id,company=request.user.company_id)
        if document:
            return render(request, 'document_panel/detail_document.html', {'document':document,'title':'Döküman'})
        else: return redirect('https://dormoni.com/document_panel/document_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def table_document(request,student_id):
    if request.user.has_perm('document_panel.change_documentinfomodel'):
        document_list=DocumentInfoModel.objects.filter(company=request.user.company_id)
        if student_id: document_list=document_list.filter(person=student_id)
        return render(request, 'document_panel/table_document.html', {'document_list':document_list,'title':'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def edit_document(request,document_id):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id,company=request.user.company_id)
        formdocument = DocumentInfoForm(user=request.user,instance=document,initial={'image_field':document.image_field})
        if request.method=='POST':
            formdocument=DocumentInfoForm(user=request.user,POST=request.POST,FILES=request.FILES,instance=document)
            if formdocument.is_valid():
                formdocument.save()
                return redirect('https://dormoni.com/document_panel/document_table/')
        return render(request,'document_panel/add_document.html',{'form':formdocument,'title':'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def delete_document(request,document_id):
    if request.user.has_perm('document_panel.add_documentinfomodel'):
        document=DocumentInfoModel.objects.get(pk=document_id,company=request.user.company_id)
        document.delete()
        return redirect('https://dormoni.com/document_panel/document_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')


def liability_add(request):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        formliability=LiabilityInfoForm(user=request.user)
        if request.POST:
            formliability=LiabilityInfoForm(user=request.user,POST=request.POST)
            if formliability.is_valid():
                formliability.save()
                return redirect('https://dormoni.com/document_panel/liability_table/')
        return render(request,'document_panel/add_liability.html',{'form':formliability,'title':'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def liability_detail(request,record_no):
    if request.user.has_perm('document_panel.change_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no,company=request.user.company_id)
        if liability:
            return render(request,'document_panel/detail_liability.html',{'liability':liability,'title':'Döküman'})
        else: return redirect('https://dormoni.com/document_panel/liability_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')

def liability_table(request,student_id):
    if request.user.has_perm('document_panel.change_liabilityinfomodel'):
        liability_list=LiabilityInfoModel.objects.filter(company=request.user.company_id)
        if student_id: liability_list=liability_list.filter(person=student_id)
        return render(request,'document_panel/table_liability.html',{'liability_list':liability_list,'title':'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def liability_edit(request,record_no):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        liability=LiabilityInfoModel.objects.get(pk=record_no,company=request.user.company_id)
        formliability=LiabilityInfoForm(user=request.user,instance=liability)
        if request.method=='POST':
            formliability=LiabilityInfoForm(user=request.user,POST=request.POST,instance=liability)
            if formliability.is_valid():
                formliability.save()
            return redirect('https://dormoni.com/document_panel/liability_table/')
        return render(request, 'document_panel/add_liability.html',{'form': formliability, 'title': 'Döküman'})
    else: return redirect('https://dormoni.com/user_panel/login/')

def liability_delete(request,record_no):
    if request.user.has_perm('document_panel.add_liabilityinfomodel'):
        LiabilityInfoModel.objects.get(pk=record_no,company=request.user.company_id).delete()
        return redirect('https://dormoni.com/document_panel/liability_table/')
    else: return redirect('https://dormoni.com/user_panel/login/')
