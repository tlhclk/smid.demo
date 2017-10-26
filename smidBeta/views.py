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

def page_not404_found(request):
    response= render(request,'404.html',{'title':'404 Not Found'})
    response.status_code=404
    return response

def page_not403_found(request):
    response= render(request,'403.html',{'title':'403 Forbidden'})
    response.status_code=403
    return response

def page_not400_found(request):
    response= render(request,'400.html',{'title':'400 Bad Request'})
    response.status_code=400
    return response

def page_not500_found(request):
    response= render(request,'500.html',{'title':'500 Internal Server Error'})
    response.status_code=500
    return response
