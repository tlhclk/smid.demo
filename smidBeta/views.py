# -*- coding: utf-8 -*-

from django.shortcuts import render

def home_page(request):
    return render(request,'home_page.html')

def contract(request):
    return render(request,'contract.html')

def rules(request):
    return render(request,'rules.html')
