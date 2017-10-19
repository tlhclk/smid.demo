# -*- coding: utf-8 -*-

from django.shortcuts import render

def home_page(request):
    return render(request,'home_page.html',{'title':'Ana Sayfa'})

def main_page(request):
    return render(request,'main_page.html',{'title':'Ana Sayfa'})

def contract(request):
    return render(request,'contract.html',{'title':'Sözleşme'})

def rules(request):
    return render(request, 'rules.html', {'title': 'Kurallar'})
