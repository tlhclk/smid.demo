# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import DocumentInfoModel
from .forms import DocumentInfoForm



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
